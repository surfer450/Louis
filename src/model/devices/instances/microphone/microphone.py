from src.model.devices.abstract_device import Device
from src.model.streams.instances.microphone.microphone_stream import MicrophoneStream
from src.observability.configuration_handlers.abstract_configuration_handler import AbstractConfigurationHandler
from src.observability.logging_handler.abstract_logging_handler import AbstractLoggingHandler


class Microphone(Device):
    """
    A class representing a microphone device.

    This class inherits from the `Device` class and provides functionality to interact with a microphone device.
    It initializes a microphone stream using the `MicrophoneStream` class, enabling operations like opening, closing,
    and capturing audio from the microphone. The microphone's configuration and logging are managed by external
    handlers passed during instantiation.
    """

    def __init__(self, microphone_index: int, configuration_handler: type(AbstractConfigurationHandler),
                 logging_handler: type(AbstractLoggingHandler)):
        """
        Initializes the Microphone device with the given configuration handler and logging handler.

        Args:
            microphone_index (int): The index of the microphone device.
            configuration_handler (AbstractConfigurationHandler): The handler for configuration settings.
            logging_handler (AbstractLoggingHandler): The handler for logging operations.
        """
        super().__init__(device_index=microphone_index, configuration_handler=configuration_handler,
                         logging_handler=logging_handler)
        self.stream = MicrophoneStream(self.device_index, self.config, self.logger)
