from abc import ABC
from queue import Queue

from src.observability.logging_handler.instances.basic_logging_handler import BasicLoggingHandler


class Device(ABC):
    """
    Abstract base class representing a device that can record audio (or other data).
    This class defines the basic structure for interacting with a device, starting and stopping
    recordings, and retrieving data from the stream.
    """

    def __init__(self, device_index: int):
        """
        Initializes the Device class with necessary parameters like device index, logging handler,
        and configuration handler.

        Args:
            device_index (int): Index of the device.
        """
        self.device_index = device_index
        self.is_recording = False
        self.logger = BasicLoggingHandler.get_logging_handler().logger

    async def start_device_recording(self, output_queue) -> None:
        """
        Starts recording from the device by opening the stream and ensuring it's activated.

        If the stream is not open, it attempts to open it. If the stream cannot be activated,
        it raises a DeviceOpenException.
        """

    def stop_device_recording(self) -> None:
        """
        Stops the recording by closing the device stream.

        Closes the stream if it's open and sets the recording state to False.
        """
