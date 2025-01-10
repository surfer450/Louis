from abc import ABC, abstractmethod
from typing import Any
from src.exceptions.device_exceptions import DeviceOpenException, DeviceNotRecordingException


class Device(ABC):
    """
    Abstract base class representing a device that can record audio (or other data).
    This class defines the basic structure for interacting with a device, starting and stopping
    recordings, and retrieving data from the stream.
    """

    def __init__(self, device_index, logging_handler, configuration_handler):
        """
        Initializes the Device class with necessary parameters like device index, logging handler,
        and configuration handler.

        Args:
            device_index (int): Index of the device.
            logging_handler (LoggingHandler): Handler for logging activities.
            configuration_handler (ConfigurationHandler): Handler for retrieving configuration details.
        """
        self.device_index = device_index
        self.logger = logging_handler.get_logging_handler().logger
        self.config = configuration_handler.get_configuration_handler().config
        self.is_recording = False
        self.device_name = f"{self.__class__.__name__} {self.device_index}"
        self.stream = None

    @abstractmethod
    def open_stream(self):
        """
        Opens the device's stream for recording.

        This method must be implemented by a subclass of Device. It should handle the logic
        for opening a device stream for recording data.
        """
        pass

    @abstractmethod
    def close_stream(self):
        """
        Closes the device's stream.

        This method must be implemented by a subclass of Device. It should handle the logic
        for closing the device stream once recording is finished.
        """
        pass

    @abstractmethod
    def is_stream_activate(self):
        """
        Checks if the device stream is active.

        This method must be implemented by a subclass of Device. It should return a boolean
        indicating whether the device's stream is currently active.

        Returns:
            bool: True if the stream is active, False otherwise.
        """
        pass

    @abstractmethod
    def get_stream_data(self):
        """
        Retrieves data from the active device stream.

        This method must be implemented by a subclass of Device. It should return the
        data captured from the device's stream.

        Returns:
            Any: Data from the device stream.
        """
        pass

    def start_device_recording(self) -> None:
        """
        Starts recording from the device by opening the stream and ensuring it's activated.

        If the stream is not open, it attempts to open it. If the stream cannot be activated,
        it raises a DeviceOpenException.
        """
        if self.stream is None:
            self.open_stream()

        if not self.is_stream_activate():
            self.logger.error(f"Failed to activate {self.device_name}")
            raise DeviceOpenException(device_name=self.device_name)

        self.is_recording = True
        self.logger.debug(f"{self.device_name} opened successfully!")

    def stop_device_recording(self) -> None:
        """
        Stops the recording by closing the device stream.

        Closes the stream if it's open and sets the recording state to False.
        """
        if self.stream:
            self.close_stream()
        self.stream = None
        self.is_recording = False
        self.logger.debug(f"{self.device_name} closed successfully!")

    def device_recording_logic(self) -> Any:
        """
        Retrieves data from the device's stream if it is currently recording.

        This method checks whether the device is recording, whether the stream is active,
        and then calls the appropriate method to retrieve the stream's data.

        Returns:
            Any: Data from the device's stream.
        """
        if not self.is_recording or not self.stream or not self.is_stream_activate():
            self.logger.error(f"{self.device_name} is not recording.")
            raise DeviceNotRecordingException(device_name=self.device_name)

        return self.get_stream_data()
