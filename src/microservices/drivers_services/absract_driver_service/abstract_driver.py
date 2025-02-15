import asyncio
import threading
from abc import ABC, abstractmethod
from asyncio import Queue
from typing import Any
from src.microservices.drivers_services.absract_driver_service.abstract_device import Device
from src.observability.logging_handler.instances.basic_logging_handler import BasicLoggingHandler


class Driver(ABC):
    def __init__(self, device: Device):
        self.device = device
        self.inner_input_driver_queue = Queue()
        self.inner_validated_data_deriver_dict = {}
        self.current_sequence_id = 0
        self.lock = asyncio.Lock()
        self.inner_accumulating_driver_queue = Queue()
        self.external_output_driver_queue = Queue()
        self.logger = BasicLoggingHandler.get_logging_handler().logger

    async def activate_driver(self) -> None:
        await asyncio.gather(
            self.device.start_device_recording(self.inner_input_driver_queue),
            self.process_input_data(),
            self.process_validated_data(),
            self.process_output_data()
        )

    async def process_input_data(self) -> None:
        sequence_id = 0
        while True:
            data = await self.inner_input_driver_queue.get()
            print(data)
            task = asyncio.create_task(self.is_input_data_valid(data, sequence_id))
            sequence_id += 1

    async def is_input_data_valid(self, data: Any, sequence_id: int) -> None:
        if await self.input_validation_logic(data):
            async with self.lock:
                self.inner_validated_data_deriver_dict[sequence_id] = data

    @abstractmethod
    async def input_validation_logic(self, data: Any) -> bool:
        pass

    async def process_validated_data(self):
        while True:
            async with self.lock:
                if self.current_sequence_id in self.inner_validated_data_deriver_dict.keys():
                    await self.inner_accumulating_driver_queue.put(
                        self.inner_validated_data_deriver_dict[self.current_sequence_id]
                    )
                    self.inner_validated_data_deriver_dict.pop(self.current_sequence_id)
                    self.current_sequence_id += 1
                    await self.update_metadata_in_insertion()

    @abstractmethod
    async def update_metadata_in_insertion(self):
        pass

    async def process_output_data(self) -> None:
        while True:
            if await self.is_output_data_valid():
                await self.external_output_driver_queue.put(self.inner_accumulating_driver_queue)

    @abstractmethod
    async def is_output_data_valid(self) -> bool:
        pass
