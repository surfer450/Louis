import threading
from abc import ABC, abstractmethod
from queue import Queue
from typing import Any
from src.observability.logging_handler.instances.basic_logging_handler import BasicLoggingHandler
from src.shared_logic.abstract_accumulators.abstract_accumulator import Accumulator


class Driver(ABC):
    def __init__(self, accumulator: Accumulator):
        self.accumulator = accumulator
        self.is_recording = False
        self.thread = None
        self.logger = BasicLoggingHandler.get_logging_handler().logger

    def start_driver_action(self, input_queue: Queue, output_queue: Queue):
        self.is_recording = True
        self.thread = threading.Thread(target=self.driver_action_logic, args=(input_queue, output_queue,)).start()

    def driver_action_logic(self, input_queue: Queue, output_queue: Queue) -> None:
        while True:
            data = input_queue.get()
            if self.is_input_data_valid(data):
                self.accumulator.insert_data(data)
                self.input_activation()

            if self.is_output_data_valid():
                output_queue.put(self.accumulator)
                self.output_activation()

    def stop_driver_action(self):
        self.is_recording = False
        self.thread.join()

    @abstractmethod
    def is_input_data_valid(self, data: Any) -> bool:
        pass

    @abstractmethod
    def input_activation(self) -> None:
        pass

    @abstractmethod
    def is_output_data_valid(self) -> bool:
        pass

    @abstractmethod
    def output_activation(self) -> None:
        pass
