from numpy import ndarray, std, mean
from cv2 import cvtColor, COLOR_BGR2GRAY

from src.model.device_track.abstract_track.abstract_validator import Validator
from src.model.device_track.instances.shared_logic.helpers.data_context import DataContext
from src.observability.configuration_handlers.instances.CameraValidatorConfigurationHandler import \
    CameraDeviceConfigurationHandler
from src.observability.logging_handler.instances.basic_logging_handler import BasicLoggingHandler


class CameraValidator(Validator):
    DEFAULT_VALIDATORS = [
        "validate_brightness",
        "validate_variation"
    ]
    Config = CameraDeviceConfigurationHandler.get_configuration_handler().config
    Logger = BasicLoggingHandler.get_logging_handler().logger

    @staticmethod
    def convert_to_grayscale(frame: ndarray) -> ndarray:
        return cvtColor(frame, COLOR_BGR2GRAY)

    @staticmethod
    def validate_brightness(context: DataContext) -> bool:
        """
        Check if the frame's brightness is above a certain threshold.
        :param context: DataContext containing data and metadata.
        :return: True if brightness is sufficient, False otherwise.
        """
        frame = context.data
        gray = CameraValidator.convert_to_grayscale(frame)
        mean_brightness = mean(gray)
        if mean_brightness < CameraValidator.Config["brightness_threshold"]:
            CameraValidator.Logger.debug("Frame is invalid: Too dark")
            return False
        return True

    @staticmethod
    def validate_variation(context: DataContext) -> bool:
        """
        Check if the frame has sufficient variation (not uniform).
        :param context: DataContext containing data and metadata.
        :return: True if variation is sufficient, False otherwise.
        """
        frame = context.data
        gray = CameraValidator.convert_to_grayscale(frame)
        standard_deviation = std(gray)
        if standard_deviation < CameraValidator.Config["standard_deviation_threshold"]:
            CameraValidator.Logger.debug("Frame is invalid: Too uniform (unrecognizable)")
            return False
        return True
