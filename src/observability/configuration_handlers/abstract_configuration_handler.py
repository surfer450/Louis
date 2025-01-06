from abc import ABC, abstractmethod
from json import loads
from typing import TypeVar, Dict
from src.observability.configuration_handlers.shared_logic.helpers.configuration_reader import ConfigurationReader

ConfigurationHandlerType = TypeVar("ConfigurationHandlerType")


class AbstractConfigurationHandler(ABC):
    """
    AbstractConfigurationHandler serves as a base class for handling configuration management
    in a standardized way. It provides methods to retrieve and update a configuration handler
    from a specified configuration file.

    The class relies on a configuration file path and a configuration reader to load the configuration.

    Attributes:
        config_handler (Dict): A dictionary that holds the current configuration handler.
                               Initialized to None and updated via `update_config_handler`.
        config_file_path (str): The path to the configuration file from which the handler is read.
    """

    config_handler: Dict = None
    config_file_path: str = None

    @classmethod
    @abstractmethod
    def get_configuration_handler(cls) -> ConfigurationHandlerType:
        """
        An abstract method that must be implemented by subclasses to provide the logic for retrieving
        the configuration handler.

        Args:
            cls: The class invoking the method.

        Returns:
            ConfigurationHandlerType: The configuration handler instance.
        """
        pass

    @classmethod
    def update_config_handler(cls) -> None:
        """
        Updates the `config_handler` class attribute by reading the configuration file specified by
        `config_file_path`. The configuration is expected to be in JSON format and is parsed into a
        dictionary using `loads`.

        This method should be called if `config_handler` is None or needs to be refreshed.

        Args:
            cls: The class invoking the method.
        """
        cls.config_handler = loads(ConfigurationReader.read_configfile(cls.config_file_path))
