from src.observability.configuration_handlers.abstract_configuration_handler import AbstractConfigurationHandler


class MicrophoneDeviceConfigurationHandler(AbstractConfigurationHandler):
    """
    A dynamic configuration handler for camera devices.

    This class provides a mechanism to manage and update configuration
    settings for microphone devices dynamically.
    """
    def get_config_path(self) -> str:
        return "configurations/devices/camera/microphone_device_config.json"

