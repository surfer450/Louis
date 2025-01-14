from typing import Any

from numpy import int16, float32, frombuffer, sqrt, mean, ndarray, dtype
from pyaudio import PyAudio, paInt16
from src.exceptions.stream_exceptions import StreamNoOutputException, StreamWontStartException, \
    StreamWontCloseException, StreamIsInvalid
from src.model.device_track.abstract_track.abstract_stream import Stream
from src.observability.configuration_handlers.instances.microphone_device_configuration_handler import \
    MicrophoneDeviceConfigurationHandler
from src.observability.logging_handler.instances.basic_logging_handler import BasicLoggingHandler


class MicrophoneStream(Stream):
    """
    A stream class representing an audio input stream from a microphone device.

    This class provides functionality to open, close, check the status of, and read data from a microphone stream.
    It interfaces with the PyAudio library to capture audio data and process it into usable information.
    """

    def __init__(self, device_index: int):
        """
        Initializes the MicrophoneStream instance.

        This constructor sets up the microphone stream by accepting the device index, which corresponds to
        the specific microphone input device. It also initializes the logger and configuration handler,
        and prepares the microphone stream for audio capture.

        Args:
            device_index (int): The device index of the microphone to stream from. This corresponds
                                 to the microphone index in the system's device list (e.g., 0 for the first microphone,
                                 1 for the second).

        Raises:
            StreamWontStartException: If the microphone stream cannot be opened due to an error,
                                      such as an invalid device index or configuration.
        """
        super().__init__(device_index)
        self.logger = BasicLoggingHandler.get_logging_handler().logger
        self.config = MicrophoneDeviceConfigurationHandler.get_configuration_handler().config

    def open_stream(self) -> None:
        """
        Opens the microphone input stream.

        This method initializes and opens the microphone stream using PyAudio with the provided configuration.
        It configures the format, channels, sample rate, and buffer size, then starts the input stream for audio capture

        Raises:
            StreamWontStartException: If the microphone stream cannot be opened due to an error,
            such as an invalid device index or configuration.
        """
        try:
            self.stream = PyAudio().open(format=paInt16,
                                         channels=1,
                                         rate=self.config["rate"],
                                         input=True,
                                         input_device_index=self.device_index,
                                         frames_per_buffer=self.config["audio_chunk"])

        except (OSError, ValueError, AttributeError) as exception:
            self.logger.error(f"Error opening {self.__class__.__name__}")
            raise StreamWontStartException(stream_name=self.__class__.__name__, failure_reason=exception.__str__())

    def close_stream(self) -> None:
        """
        Closes the microphone input stream.

        This method stops and closes the microphone stream, releasing the resources associated with it.

        Raises:
            StreamWontCloseException: If the microphone stream cannot be closed properly due to an error.
        """
        try:
            self.stream.stop_stream()
            self.stream.close()
            self.stream = None

        except (OSError, ValueError, AttributeError) as exception:
            self.logger.error(f"Error closing {self.__class__.__name__}")
            raise StreamWontCloseException(stream_name=self.__class__.__name__, failure_reason=exception.__str__())

    def is_stream_active(self) -> bool:
        """
        Checks if the microphone stream is currently active.

        This method checks if the microphone stream is open and actively capturing data.

        Returns:
            bool: True if the stream is active, False if the stream is closed or inactive.

        Raises:
            StreamIsInvalid: If the stream is not initialized or is in an invalid state.
        """
        try:
            return self.stream.is_active()

        except (OSError, ValueError, AttributeError) as exception:
            self.logger.error(f"Error accessing {self.__class__.__name__}")
            raise StreamIsInvalid(stream_name=self.__class__.__name__, failure_reason=exception.__str__())

    def get_stream_data(self) -> tuple[ndarray[tuple[int, ...], dtype], Any]:
        """
        Retrieves audio data from the microphone stream.

        This method reads a chunk of audio data from the microphone stream, converts it to a numpy array,
        and calculates the volume of the audio data based on the root mean square (RMS) value.

        Returns:
            tuple: A tuple containing the audio data (numpy array) and the calculated volume (float).
                - data (numpy.ndarray): The audio data as a numpy array of type float32.
                - volume (float): The root mean square (RMS) volume of the audio data.

        Raises:
            StreamNoOutputException: If no audio data is retrieved from the microphone stream.
        """
        try:
            data = frombuffer(self.stream.read(self.config["audio_chunk"], exception_on_overflow=False),
                              dtype=int16).astype(float32)
            volume = sqrt(mean(data ** 2))
            return data, volume

        except Exception as exception:
            self.logger.error(f"Error reading sound from {self.__class__.__name__}")
            raise StreamNoOutputException(stream_name=self.__class__.__name__, failure_reason=exception.__str__())
