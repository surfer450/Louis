from src.model.device_track.abstract_track.abstract_device import Device
from src.model.device_track.instances.camera_track.camera_stream import CameraStream
from src.observability.configuration_handlers.abstract_configuration_handler import AbstractConfigurationHandler
from src.observability.configuration_handlers.instances.camera_device_configuration_handler import \
    CameraDeviceConfigurationHandler
from src.observability.logging_handler.abstract_logging_handler import AbstractLoggingHandler
from src.observability.logging_handler.instances.basic_logging_handler import BasicLoggingHandler


class Camera(Device):
    """
    A class representing a camera device.

    This class inherits from the `Device` class and provides functionality to interact with a camera device.
    """

    def __init__(self, camera_index: int):
        """
        Initializes the Camera device with the given configuration handler and logging handler.

        Args:
            camera_index (int): The index of the camera device.
        """
        super().__init__(device_index=camera_index)
        self.stream = CameraStream(self.device_index)
        self.logger = BasicLoggingHandler.get_logging_handler().logger
        self.config = CameraDeviceConfigurationHandler.get_configuration_handler().config
