import numpy as np
from cv2 import cvtColor, COLOR_BGR2GRAY
from typing import List, Callable
from src.model.device_track.abstract_track.abstract_validator import Validator
from src.observability.configuration_handlers.instances.CameraValidatorConfigurationHandler import \
    CameraDeviceConfigurationHandler
from src.observability.logging_handler.instances.basic_logging_handler import BasicLoggingHandler


class CameraValidator(Validator):
    DEFAULT_VALIDATORS = [
        "validate_brightness",
        "validate_variation"
    ]

    def __init__(self, validation_functions: List[Callable] = None):
        """
        Initialize the CameraValidator with a list of validation functions.
        :param validation_functions: List of validation functions to apply by default.
        """
        super().__init__(validation_functions)
        self.logger = BasicLoggingHandler.get_logging_handler().logger
        self.config = CameraDeviceConfigurationHandler.get_configuration_handler().config

    def is_valid(self, frame: np.ndarray, validation_functions: List[Callable] = None) -> bool:
        """
        Validate a frame by running it through a list of validation functions.

        :param frame: The frame (numpy array) received from the camera.
        :param validation_functions: List of validation functions to apply.
                                      If None, defaults to the instance's validation functions.
        :return: True if all validation functions pass, False otherwise.
        """
        functions = validation_functions or self.validation_functions

        for validate in functions:
            if not validate(frame):
                return False

        return True

    @staticmethod
    def convert_to_grayscale(frame: np.ndarray) -> np.ndarray:
        return cvtColor(frame, COLOR_BGR2GRAY)

    def validate_brightness(self, frame: np.ndarray) -> bool:
        """
        Check if the frame's brightness is above a certain threshold.
        :param frame: The frame (numpy array).
        :return: True if brightness is sufficient, False otherwise.
        """
        gray = CameraValidator.convert_to_grayscale(frame)
        mean_brightness = np.mean(gray)
        if mean_brightness < self.config["brightness_threshold"]:
            self.logger.debug("Frame is invalid: Too dark")
            return False
        return True

    def validate_variation(self, frame: np.ndarray) -> bool:
        """
        Check if the frame has sufficient variation (not uniform).
        :param frame: The frame (numpy array).
        :return: True if variation is sufficient, False otherwise.
        """
        gray = CameraValidator.convert_to_grayscale(frame)
        standard_deviation = np.std(gray)
        if standard_deviation < self.config["standard_deviation_threshold"]:
            self.logger.debug("Frame is invalid: Too uniform (unrecognizable)")
            return False
        return True
