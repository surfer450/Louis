from abc import ABC
from typing import TypeVar, Any, Dict
ConfigurationHandlerType = TypeVar("ConfigurationHandlerType")


class AbstractConfigurationHandler(ABC):
    config_handler: Dict = None
    config_file_path: str = None

    @staticmethod
    def get_configuration_handler() -> ConfigurationHandlerType:
        pass
