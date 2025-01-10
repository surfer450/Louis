from logging import Logger
from typing import Any, Tuple
import numpy as np
import pyaudio

from src.exceptions.device_exceptions import (
    DeviceOpenException,
    DeviceNotRecordingException,
    DeviceNoOutputException
)
from src.model.devices.abstract_device import Device


class Microphone(Device):
    """
    A class representing a microphone device that can record audio input.

    Attributes:
        logger (Logger): Logger for logging information and errors.
        microphone_index (int): The index of the microphone device.
        audio_chunk (int): The size of the audio buffer to read at a time.
        rate (int): The sample rate for audio input.
        volume_threshold (int): Threshold for detecting significant sound volume.
        pyaudio_object (pyaudio.PyAudio): Instance of PyAudio for audio handling.
        stream (pyaudio.Stream): Audio stream for recording.
        is_recording (bool): Indicates if the microphone is currently recording.
        device_name (str): Name of the microphone device.
    """

    def __init__(self, logger: Logger, microphone_index: int):
        """
        Initializes the Microphone object.

        Args:
            logger (Logger): Logger instance for logging messages.
            microphone_index (int): The index of the microphone device to use.
        """
        self.audio_chunk = 1024
        self.rate = 44100
        self.volume_threshold = 1000
        self.pyaudio_object = pyaudio.PyAudio()
        self.stream = None

        self.microphone_index = microphone_index
        self.is_recording = False
        self.logger = logger
        self.device_name = f"Microphone {self.microphone_index}"

    def start_device_recording(self) -> None:
        """
        Starts recording audio from the microphone.

        Raises:
            DeviceOpenException: If the microphone cannot be opened or activated.
        """
        if self.stream is None:
            try:
                self.stream = self.pyaudio_object.open(format=pyaudio.paInt16,
                                                       channels=1,
                                                       rate=self.rate,
                                                       input=True,
                                                       input_device_index=self.microphone_index,
                                                       frames_per_buffer=self.audio_chunk)
            except (OSError, ValueError) as e:
                self.logger.error(f"Failed to start {self.device_name}: {e}")
                raise DeviceOpenException(device_name=self.device_name)

        if not self.stream.is_active():
            self.logger.error(f"Failed to activate {self.device_name}")
            raise DeviceOpenException(device_name=self.device_name)

        self.is_recording = True
        self.logger.debug(f"{self.device_name} opened successfully!")

    def stop_device_recording(self) -> None:
        """
        Stops recording audio from the microphone.
        """
        if self.stream:
            self.stream.stop_stream()
            self.stream.close()
            self.stream = None
        self.is_recording = False
        self.logger.debug("Microphone recording stopped.")

    def device_recording_logic(self) -> Tuple[np.ndarray, float]:
        """
        Performs the recording logic, capturing audio data and calculating volume.

        Returns:
            Tuple[np.ndarray, float]: The audio data as a numpy array and the calculated volume.

        Raises:
            DeviceNotRecordingException: If the microphone is not recording.
        """
        if not self.is_recording or not self.stream or not self.stream.is_active():
            self.logger.error(f"{self.device_name} is not recording.")
            raise DeviceNotRecordingException(device_name=self.device_name)

        return self.get_sound()

    def get_sound(self) -> Tuple[np.ndarray, float]:
        """
        Captures sound data from the microphone and calculates its volume.

        Returns:
            Tuple[np.ndarray, float]: The audio data as a numpy array and the calculated volume.

        Raises:
            DeviceNoOutputException: If an error occurs while reading audio data.
        """
        try:
            data = np.frombuffer(self.stream.read(self.audio_chunk, exception_on_overflow=False),
                                 dtype=np.int16).astype(np.float32)
            volume = np.sqrt(np.mean(data ** 2))
            return data, volume

        except Exception as e:
            self.logger.error(f"Error reading sound from {self.device_name}: {e}")
            raise DeviceNoOutputException(device_name=self.device_name)
