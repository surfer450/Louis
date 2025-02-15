import asyncio

from numpy import int16, float32, frombuffer, sqrt, mean, ndarray, dtype
from pyaudio import PyAudio, paInt16
from pyaudio import PyAudio, paInt16

from src.microservices.drivers_services.device_exceptions import DeviceWontStartException, DeviceWontCloseException
from src.microservices.drivers_services.absract_driver_service.abstract_device import Device


class Microphone(Device):
    """
    A class representing a microphone device.

    This class inherits from the `Device` class and provides functionality to interact with a microphone device.
    It initializes a microphone stream using the `MicrophoneStream` class, enabling operations like opening, closing,
    and capturing audio from the microphone. The microphone's configuration and logging are managed by external
    handlers passed during instantiation.
    """

    def __init__(self, microphone_index: int, rate: int, audio_chunk: int):
        """
        Initializes the Microphone device with the given configuration handler and logging handler.

        Args:
            microphone_index (int): The index of the microphone device.
        """
        super().__init__(device_index=microphone_index)
        self.rate = rate
        self.audio_chunk = audio_chunk
        self.stream = PyAudio().open(format=paInt16,
                                     channels=1,
                                     rate=self.rate,
                                     input=True,
                                     input_device_index=self.device_index,
                                     frames_per_buffer=self.audio_chunk)

    async def start_device_recording(self, output_queue) -> None:
        """
        Starts recording from the device by opening the stream and ensuring it's activated.

        If the stream is not open, it attempts to open it. If the stream cannot be activated,
        it raises a DeviceOpenException.
        """
        try:
            loop = asyncio.get_running_loop()
            while True:
                raw_data = await loop.run_in_executor(
                    None,  # Uses the default ThreadPoolExecutor
                    self.stream.read,  # Function to run
                    self.audio_chunk,  # First argument
                    False  # exception_on_overflow=False
                )
                data = frombuffer(raw_data, dtype=int16).astype(float32)
                print(data)
                await output_queue.put(data)

        except (OSError, ValueError, AttributeError) as exception:
            self.logger.error(f"Error opening {self.__class__.__name__}")
            raise DeviceWontStartException(device_name=self.__class__.__name__, failure_reason=exception.__str__())

    def stop_device_recording(self) -> None:
        """
        Stops the recording by closing the device stream.

        Closes the stream if it's open and sets the recording state to False.
        """
        pass
