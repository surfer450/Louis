from abc import ABC, abstractmethod
from json import load
from logging import getLogger, Logger
from logging import config
from threading import Lock
from typing import TypeVar

LoggerHandlerType = TypeVar("LoggerHandlerType")


class AbstractLoggingHandler(ABC):
    """
    A singleton class that provides logging functionality using a shared logger instance.

    This class initializes a logger using configurations from a JSON file and provides methods
    to access the logger instance with thread-safety using a lock.
    """
    _shared_logger_handler = None

    def __init__(self):
        """
        Initializes the LoggerHandler instance, sets up a lock for thread-safety,
        and initializes the logger using the logging configuration file.
        """
        self._logger = None
        self.initialize_logger()

    @abstractmethod
    def initialize_logger(self) -> None:
        """
        Initializes the logger by loading the configuration from a JSON file and setting it up
        using the logging module's dictConfig.

        The configuration file should be located at 'configurations/logging_config.json'.
        """
        pass

    @property
    def logger(self) -> Logger:
        """
        Gets the logger instance.

        Returns:
            Logger: The logger instance configured for the application.
        """
        return self._logger

    @logger.setter
    def logger(self, value: Logger) -> None:
        """
        Sets the logger instance.

        Args:
            value (Logger): The logger instance to be assigned.
        """
        self._logger = value

    @classmethod
    def get_logging_handler(cls) -> LoggerHandlerType:
        """
        Retrieves the singleton instance of the LoggerHandler class.

        If the instance does not exist, it creates one.

        Returns:
            LoggerHandlerType: The singleton LoggerHandler instance.
        """
        if cls._shared_logger_handler is None:
            cls._shared_logger_handler = cls()
        return cls._shared_logger_handler
