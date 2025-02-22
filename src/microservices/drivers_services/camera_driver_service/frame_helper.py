from cv2 import cvtColor, COLOR_BGR2GRAY
from numpy import mean, ndarray, floating, std
from typing import Any


class FrameHelper:
    @staticmethod
    def convert_to_grayscale(frame: ndarray) -> ndarray:
        return cvtColor(frame, COLOR_BGR2GRAY)

    @staticmethod
    def get_frame_brightness(frame: ndarray) -> floating[Any]:
        """
        Check if the frame's brightness is above a certain threshold.
        :param frame: DataContext containing data and metadata.
        :return: True if brightness is sufficient, False otherwise.
        """
        gray = FrameHelper.convert_to_grayscale(frame)
        mean_brightness = mean(gray)
        return mean_brightness

    @staticmethod
    def get_frame_variation(frame: ndarray) -> floating[Any]:
        """
        Check if the frame has sufficient variation (not uniform).
        :param frame: DataContext containing data and metadata.
        :return: True if variation is sufficient, False otherwise.
        """
        gray = FrameHelper.convert_to_grayscale(frame)
        standard_deviation = std(gray)
        return standard_deviation
