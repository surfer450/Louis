import json
import logging
from logging import config
import threading
from typing import TypeVar
LoggerHandlerType = TypeVar("LoggerHandlerType")


class LoggerHandler:
    _shared_logger_handler = None
    _lock = threading.Lock()

    def __init__(self):
        self._logger = None

    def init(self, config_path="configurations/logging_config.json"):
        """Initialize logging configuration and create the logger instance."""
        with open(config_path) as configuration_file:
            dict_configuration = json.load(configuration_file)
        config.dictConfig(dict_configuration)
        self._logger = logging.getLogger("LouisLogger")

    @property
    def logger(self) -> logging.Logger:
        """Access the logger property."""
        return self._logger

    @logger.setter
    def logger(self, value: logging.Logger) -> None:
        """Set the logger manually if needed."""
        self._logger = value

    @staticmethod
    def get_logger_handler(config_path="configurations/logging_config.json") -> LoggerHandlerType:
        """Retrieve a singleton instance of LoggerHandler."""
        with LoggerHandler._lock:
            if LoggerHandler._shared_logger_handler is None:
                LoggerHandler._shared_logger_handler = LoggerHandler()
                LoggerHandler._shared_logger_handler.init(config_path)
            return LoggerHandler._shared_logger_handler
