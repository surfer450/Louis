from src.model.device_track.abstract_track.abstract_validator import Validator
from src.model.device_track.instances.shared_logic.helpers.data_context import DataContext
from src.observability.configuration_handlers.instances.microphone_device_configuration_handler import \
    MicrophoneDeviceConfigurationHandler
from src.observability.logging_handler.instances.basic_logging_handler import BasicLoggingHandler


class MicrophoneValidator(Validator):
    DEFAULT_VALIDATORS = [
        "volume_validation"
    ]
    Config = MicrophoneDeviceConfigurationHandler.get_configuration_handler().config
    Logger = BasicLoggingHandler.get_logging_handler().logger

    @staticmethod
    def volume_validation(context: DataContext) -> bool:
        """
        Checks if the volume of the incoming sound data meets the minimum threshold for legal insertion.

        :param context: DataContext containing data and metadata.
        Returns:
            bool: True if the volume exceeds the threshold defined in the configuration, otherwise False.
        """
        volume = context.metadata["volume"]
        if volume < MicrophoneValidator.Config["volume_threshold"]:
            MicrophoneValidator.Logger.debug(f"Speech volume too low")
            return False
        return True

