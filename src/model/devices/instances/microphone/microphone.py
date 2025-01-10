from typing import Tuple
from numpy import ndarray, int16, float32, frombuffer, sqrt, mean
from pyaudio import PyAudio, paInt16
from src.exceptions.device_exceptions import (
    DeviceOpenException,
    DeviceNotRecordingException,
    DeviceNoOutputException
)
from src.model.devices.abstract_device import Device
from src.observability.configuration_handlers.abstract_configuration_handler import AbstractConfigurationHandler
from src.observability.logging_handler.abstract_logging_handler import AbstractLoggingHandler


class Microphone(Device):

    def __init__(self, microphone_index: int, configuration_handler: AbstractConfigurationHandler,
                 logging_handler: AbstractLoggingHandler):

        super().__init__(device_index=microphone_index, configuration_handler=configuration_handler,
                         logging_handler=logging_handler)
        self.pyaudio_object = PyAudio()

    def open_stream(self):
        self.stream = self.pyaudio_object.open(format=paInt16,
                                               channels=1,
                                               rate=self.config["rate"],
                                               input=True,
                                               input_device_index=self.device_index,
                                               frames_per_buffer=self.config["audio_chunk"])

    def close_stream(self):
        self.stream.stop_stream()
        self.stream.close()

    def is_stream_activate(self):
        return self.stream.is_active()

    def get_stream_data(self):
        try:
            data = frombuffer(self.stream.read(self.config["audio_chunk"], exception_on_overflow=False),
                              dtype=int16).astype(float32)
            volume = sqrt(mean(data ** 2))
            return data, volume

        except Exception as e:
            self.logger.error(f"Error reading sound from {self.device_name}: {e}")
            raise DeviceNoOutputException(device_name=self.device_name, content_name="audio")

