from abc import ABC, abstractmethod
from json import loads
from typing import TypeVar, Dict
from src.observability.configuration_handlers.shared_logic.helpers.configuration_reader import ConfigurationReader
ConfigurationHandlerType = TypeVar("ConfigurationHandlerType")


class AbstractConfigurationHandler(ABC):
    config_handler: Dict = None
    config_file_path: str = None

    @staticmethod
    @abstractmethod
    def get_configuration_handler() -> ConfigurationHandlerType:
        pass

    @staticmethod
    def update_config_handler() -> None:
        AbstractConfigurationHandler._config_handler = loads(
            ConfigurationReader.read_configfile(AbstractConfigurationHandler.config_file_path))
