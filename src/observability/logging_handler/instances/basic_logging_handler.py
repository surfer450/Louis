from json import load
from logging import getLogger
from logging import config
from src.observability.logging_handler.abstract_logging_handler import AbstractLoggingHandler


class BasicLoggingHandler(AbstractLoggingHandler):
    """
    A singleton class that provides logging functionality using a shared logger instance.

    This class initializes a logger using configurations from a JSON file and provides methods
    to access the logger instance with thread-safety using a lock.
    """

    def initialize_logger(self):
        """
        Initializes the logger by loading the configuration from a JSON file and setting it up
        using the logging module's dictConfig.

        The configuration file should be located at 'configurations/logging_config.json'.
        """
        with open("configurations/logging_config.json") as configuration_file:
            dict_configuration = load(configuration_file)
        config.dictConfig(dict_configuration)
        self.logger = getLogger("LouisLogger")
