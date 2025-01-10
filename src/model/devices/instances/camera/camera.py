from src.model.devices.abstract_device import Device
from src.model.streams.instances.camera.camera_stream import CameraStream
from src.observability.configuration_handlers.abstract_configuration_handler import AbstractConfigurationHandler
from src.observability.logging_handler.abstract_logging_handler import AbstractLoggingHandler


class Camera(Device):
    """
    A class representing a camera device.

    This class inherits from the `Device` class and provides functionality to interact with a camera device.
    """

    def __init__(self, camera_index: int, configuration_handler: type(AbstractConfigurationHandler),
                 logging_handler: type(AbstractLoggingHandler)):
        """
        Initializes the Camera device with the given configuration handler and logging handler.

        Args:
            camera_index (int): The index of the camera device.
            configuration_handler (AbstractConfigurationHandler): The handler for configuration settings.
            logging_handler (AbstractLoggingHandler): The handler for logging operations.
        """
        super().__init__(device_index=camera_index, configuration_handler=configuration_handler,
                         logging_handler=logging_handler)
        self.stream = CameraStream(self.device_index, self.config, self.logger)
