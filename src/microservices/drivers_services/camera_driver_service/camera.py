import asyncio

from cv2 import VideoCapture, error as cv2error, flip

from src.microservices.drivers_services.device_exceptions import DeviceWontStartException, DeviceWontCloseException, \
    DeviceNoOutputException
from src.microservices.drivers_services.absract_driver_service.abstract_device import Device


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
        super().__init__(camera_index)
        self.video_capture = VideoCapture(self.device_index)

    async def start_device_recording(self, output_queue) -> None:
        """
        Starts recording from the device by opening the stream and ensuring it's activated.

        If the stream is not open, it attempts to open it. If the stream cannot be activated,
        it raises a DeviceOpenException.
        """

        try:
            while True:
                ret, frame = self.video_capture.read()
                if not ret:
                    self.logger.error(f"Error reading frames from {self.__class__.__name__}")
                    raise DeviceNoOutputException(device_name=self.__class__.__name__,
                                                  failure_reason="Error reading frames")
                await output_queue.put(frame)

        except (ValueError, AttributeError, cv2error) as exception:
            self.logger.error(f"Error opening {self.__class__.__name__}")
            raise DeviceWontStartException(device_name=self.__class__.__name__, failure_reason=exception.__str__())

        except asyncio.CancelledError:
            self.logger.info("Input data processing task was cancelled.")

    def stop_device_recording(self) -> None:
        """
        Stops the recording by closing the device stream.

        Closes the stream if it's open and sets the recording state to False.
        """
        pass
