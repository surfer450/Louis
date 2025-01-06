from abc import ABC, abstractmethod
from typing import Any


class Device(ABC):
    """
    Abstract base class that defines the interface for devices that handle
    recording logic (e.g., cameras, microphones).

    This class allows starting, stopping, and controlling the recording
    state, as well as defining the logic for processing the recorded data.
    """

    @abstractmethod
    def start_device_recording(self) -> None:
        """
        Starts the recording process for the device.
        """
        pass

    @abstractmethod
    def stop_device_recording(self) -> None:
        """
        Stops the recording process for the device.
        """
        pass

    @abstractmethod
    def device_recording_logic(self) -> Any:
        """
        Contains the logic for handling the data recording process.

        Returns:
            Any: The processed or raw data captured by the device (e.g., video frames, audio clips).
        """
        pass
