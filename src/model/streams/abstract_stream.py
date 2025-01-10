from abc import ABC, abstractmethod


class Stream(ABC):
    """
    Abstract base class representing a stream from a device (e.g., camera, microphone, etc.).

    This class serves as a blueprint for different types of streams that interact with hardware devices.
    It defines the core methods that should be implemented by any subclass to handle stream operations
    """

    def __init__(self, device_index, config, logger):
        """
        Initializes the Stream object with the necessary parameters.

        Args:
            device_index (int): The index or identifier of the device to stream from.
            config (dict): Configuration settings for the stream.
            logger (Logger): Logger instance for logging information and errors related to the stream.
        """
        self.device_index = device_index
        self.config = config
        self.logger = logger
        self.stream = None

    @abstractmethod
    def open_stream(self):
        """
        Opens the stream from the device.

        This method should initialize and configure the stream (e.g., opening a camera or a microphone).

        Raises:
            StreamWontStartException: If the stream cannot be opened due to an error (e.g., invalid device index).
        """
        pass

    @abstractmethod
    def close_stream(self):
        """
        Closes the stream and releases the resources.

        This method should properly close the stream and release any associated resources (e.g., camera, microphone).

        Raises:
            StreamWontCloseException: If the stream cannot be closed properly.
        """
        pass

    @abstractmethod
    def is_stream_active(self):
        """
        Checks if the stream is currently active and open.

        Returns:
            bool: True if the stream is active, False if the stream is closed or inactive.

        Raises:
            StreamIsInvalid: If the stream is not initialized or is in an invalid state.
        """
        pass

    @abstractmethod
    def get_stream_data(self):
        """
        Retrieves the data from the stream.

        This method should capture and return the data from the stream (e.g., a frame from a camera).

        Returns:
            object: The data captured from the stream (e.g., an image frame, audio, etc.).

        Raises:
            StreamNoOutputException: If no data is returned from the stream (e.g., frame not captured, no audio).
        """
        pass
