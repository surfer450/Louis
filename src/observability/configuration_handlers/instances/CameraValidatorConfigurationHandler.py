from src.observability.configuration_handlers.abstract_configuration_handler import AbstractConfigurationHandler


class CameraDeviceConfigurationHandler(AbstractConfigurationHandler):
    """
    A dynamic configuration handler for camera validators.

    This class provides a mechanism to manage and update configuration
    settings for camera devices dynamically.
    """
    def get_config_path(self) -> str:
        return "configurations/devices/camera/camera_validator_config.json"

