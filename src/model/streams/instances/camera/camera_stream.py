from cv2 import VideoCapture, flip, error as cv2error
from src.exceptions.stream_exceptions import StreamNoOutputException, StreamWontStartException, \
    StreamWontCloseException, StreamIsInvalid
from src.model.streams.abstract_stream import Stream


class CameraStream(Stream):
    """
    A stream class representing a video input stream from a camera device. This class provides
    functionality to open, close, check the status of, and read data (video frames) from a camera stream.
    It uses OpenCV `VideoCapture` class to interact with the camera and captures frames from the video stream.
    """

    def open_stream(self):
        """
        Opens the camera input stream.

        This method initializes and opens the camera stream using OpenCV `VideoCapture` class.
        It configures the camera device based on the provided device index.

        Raises:
            StreamWontStartException: If the camera stream cannot be opened due to an error,
            such as an invalid device index or unsupported format.
        """
        try:
            self.stream = VideoCapture(self.device_index)

        except (ValueError, AttributeError, cv2error) as exception:
            self.logger.error(f"Error opening {self.__class__.__name__}")
            raise StreamWontStartException(stream_name=self.__class__.__name__, failure_reason=exception.__str__())

    def close_stream(self):
        """
        Closes the camera input stream.

        This method releases the camera stream and frees any associated resources.

        Raises:
            StreamWontCloseException: If the camera stream cannot be closed properly due to an error.
        """
        try:
            self.stream.release()

        except (AttributeError, cv2error) as exception:
            self.logger.error(f"Error closing {self.__class__.__name__}")
            raise StreamWontCloseException(stream_name=self.__class__.__name__, failure_reason=exception.__str__())

    def is_stream_active(self):
        """
        Checks if the camera stream is currently active.

        This method checks if the camera stream is open and actively capturing frames.

        Returns:
            bool: True if the stream is active, False if the stream is closed or inactive.

        Raises:
            StreamIsInvalid: If the stream is not initialized or is in an invalid state.
        """
        try:
            return self.stream.isOpened()

        except (AttributeError, cv2error) as exception:
            self.logger.error(f"Error accessing {self.__class__.__name__}")
            raise StreamIsInvalid(stream_name=self.__class__.__name__, failure_reason=exception.__str__())

    def get_stream_data(self):
        """
        Retrieves video frame data from the camera stream.

        This method reads a frame from the camera stream, flips it according to the configuration,
        and returns the captured frame.

        Returns:
            numpy.ndarray: The captured video frame after flipping, if applicable.

        Raises:
            StreamNoOutputException: If no frame is captured from the camera stream,
            or if there is an error while reading the frame.
        """
        try:
            ret, frame = self.stream.read()
            if not ret:
                self.logger.error(f"Error reading frames from {self.__class__.__name__}")
                raise StreamNoOutputException(stream_name=self.__class__.__name__,
                                              failure_reason="Error reading frames")
            frame = flip(frame, self.config["flip_value"])
            return frame

        except Exception as exception:
            self.logger.error(f"Error reading reading from {self.__class__.__name__}")
            raise StreamNoOutputException(stream_name=self.__class__.__name__,
                                          failure_reason=exception.__str__())
