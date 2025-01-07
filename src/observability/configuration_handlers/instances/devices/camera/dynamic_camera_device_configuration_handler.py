from src.observability.configuration_handlers.abstract_dynamic_configuration_handler.abstract_dynamic_configuration_handler import (
    AbstractDynamicConfigurationHandler
)


class DynamicCameraDeviceConfigurationHandler(AbstractDynamicConfigurationHandler):
    """
    A dynamic configuration handler for camera devices.

    This class provides a mechanism to manage and update configuration
    settings for camera devices dynamically.

    Attributes:
        config_file_path (str): The path to the configuration file containing the
                                camera device settings.
    """

    config_file_path = "configurations/devices/camera/camera_device_config.json"

    def __init__(self):
        """
        Initializes the configuration handler and ensures the latest
        configuration is loaded.
        """
        self.update_config_handler()
