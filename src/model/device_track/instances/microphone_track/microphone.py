from src.model.device_track.abstract_track.abstract_device import Device
from src.model.device_track.instances.microphone_track.microphone_stream import MicrophoneStream
from src.observability.configuration_handlers.instances.microphone_device_configuration_handler import \
    MicrophoneDeviceConfigurationHandler
from src.observability.logging_handler.instances.basic_logging_handler import BasicLoggingHandler


class Microphone(Device):
    """
    A class representing a microphone device.

    This class inherits from the `Device` class and provides functionality to interact with a microphone device.
    It initializes a microphone stream using the `MicrophoneStream` class, enabling operations like opening, closing,
    and capturing audio from the microphone. The microphone's configuration and logging are managed by external
    handlers passed during instantiation.
    """

    def __init__(self, microphone_index: int):
        """
        Initializes the Microphone device with the given configuration handler and logging handler.

        Args:
            microphone_index (int): The index of the microphone device.
        """
        super().__init__(device_index=microphone_index)
        self.stream = MicrophoneStream(self.device_index)
        self.logger = BasicLoggingHandler.get_logging_handler().logger
        self.config = MicrophoneDeviceConfigurationHandler.get_configuration_handler().config
