from logging import Logger
from typing import Any
from cv2 import Mat, VideoCapture, flip
from numpy import ndarray, dtype

from src.exceptions.device_exceptions import (
    DeviceOpenException,
    DeviceNotRecordingException,
    DeviceNoOutputException
)
from src.model.devices.abstract_device import Device


class Camera(Device):
    """
    Represents a camera device that captures video frames.

    Attributes:
        logger (Logger): Logger instance for logging camera activity.
        camera_index (int): Index of the camera device.
        flip_value (int): Value used to flip the captured frame.
        device_name (str): Name of the device.
        capture (VideoCapture): OpenCV VideoCapture instance.
        is_recording (bool): Flag indicating whether the camera is recording.
    """

    def __init__(self, logger: Logger, camera_index: int, flip_value: int):
        """
        Initializes the Camera instance.

        Args:
            logger (Logger): Logger instance for logging.
            camera_index (int): Index of the camera to access.
            flip_value (int): Value for flipping the captured frames.
        """
        self.capture = None
        self.is_recording = False
        self.camera_index = camera_index
        self.flip_value = flip_value
        self.logger = logger
        self.device_name = f"Camera {self.camera_index}"

    def start_device_recording(self) -> None:
        """
        Starts the recording of the camera.

        Raises:
            DeviceOpenException: If the camera cannot be opened.
        """
        if self.capture is None:
            self.capture = VideoCapture(self.camera_index)

        if not self.capture.isOpened():
            self.logger.error(f"Failed to open {self.device_name}")
            raise DeviceOpenException(device_name=self.device_name)

        self.is_recording = True
        self.logger.debug(f"{self.device_name} opened successfully!")

    def stop_device_recording(self) -> None:
        """
        Stops the recording of the camera and releases resources.
        """
        if self.capture:
            self.capture.release()
            self.capture = None
        self.is_recording = False
        self.logger.debug("Camera recording stopped.")

    def device_recording_logic(self) -> Mat | ndarray[Any, dtype] | ndarray:
        """
        Captures a frame from the camera and returns it.

        Returns:
            Mat | ndarray: Captured frame (numpy array).

        Raises:
            DeviceNotRecordingException: If the camera is not recording.
        """
        if self.is_recording and self.capture:
            return self._get_frame()
        else:
            raise DeviceNotRecordingException(device_name=self.device_name)

    def _get_frame(self):
        """
        Captures a frame from the camera and returns it.

        Returns:
            Mat | ndarray: Captured frame (numpy array).

        Raises:
            DeviceNoOutputException: If no frame is captured during recording.
        """
        ret, frame = self.capture.read()
        if not ret:
            raise DeviceNoOutputException(device_name=self.device_name, content_name="frame")
        frame = flip(frame, self.flip_value)
        return frame
