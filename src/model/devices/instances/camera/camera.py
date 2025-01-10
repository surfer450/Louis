from typing import Any
from cv2 import Mat, VideoCapture, flip
from numpy import ndarray, dtype

from src.exceptions.device_exceptions import (
    DeviceOpenException,
    DeviceNotRecordingException,
    DeviceNoOutputException
)
from src.model.devices.abstract_device import Device
from src.observability.configuration_handlers.abstract_configuration_handler import AbstractConfigurationHandler
from src.observability.logging_handler.abstract_logging_handler import AbstractLoggingHandler


class Camera(Device):

    def __init__(self, camera_index: int, configuration_handler: AbstractConfigurationHandler,
                 logging_handler: AbstractLoggingHandler):
        super().__init__(device_index=camera_index, configuration_handler=configuration_handler,
                         logging_handler=logging_handler)

    def open_stream(self):
        self.stream = VideoCapture(self.device_index)

    def close_stream(self):
        self.stream.release()

    def is_stream_activate(self):
        return self.stream.isOpened()

    def get_stream_data(self):
        ret, frame = self.stream.read()
        if not ret:
            raise DeviceNoOutputException(device_name=self.device_name, content_name="frame")
        frame = flip(frame, self.config["flip_value"])
        return frame
