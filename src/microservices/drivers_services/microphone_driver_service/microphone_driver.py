import asyncio
import time
from abc import ABC, abstractmethod
from numpy import int16, float32, frombuffer, sqrt, mean, ndarray, dtype
from asyncio import Queue
from typing import Any
from src.microservices.drivers_services.absract_driver_service.abstract_device import Device
from src.microservices.drivers_services.absract_driver_service.abstract_driver import Driver
from src.microservices.drivers_services.microphone_driver_service.microphone import Microphone
from src.observability.configuration_handlers.instances.microphone_device_configuration_handler import \
    MicrophoneDeviceConfigurationHandler
from src.observability.logging_handler.instances.basic_logging_handler import BasicLoggingHandler


class MicrophoneDriver(Driver):
    def __init__(self):
        super().__init__(Microphone(MicrophoneDeviceConfigurationHandler.get_configuration_handler().
                                    config["default_microphone_index"],
                                    MicrophoneDeviceConfigurationHandler.get_configuration_handler().
                                    config["rate"],
                                    MicrophoneDeviceConfigurationHandler.get_configuration_handler().
                                    config["audio_chunk"]))
        self.last_insertion_time = None

    async def input_validation_logic(self, data: Any) -> bool:
        volume = sqrt(mean(data ** 2))
        return volume > MicrophoneDeviceConfigurationHandler.get_configuration_handler().config["volume_threshold"]

    async def update_metadata_in_insertion(self):
        self.last_insertion_time = time.time()

    async def is_output_data_valid(self) -> bool:
        if self.last_insertion_time is None:
            return False

        time_since_last_voice = time.time() -  self.last_insertion_time
        return time_since_last_voice > MicrophoneDeviceConfigurationHandler.get_configuration_handler().config[
            "silence_time_threshold"
        ]
