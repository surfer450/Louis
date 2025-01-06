import configparser
from typing import TypeVar
ConfigurationHandlerType = TypeVar("ConfigurationHandlerType")


class AbstractConfigurationHandler:
    _shared_configuration_handler = None

    def __init__(self):
        self._config = None

    @property
    def config(self):
        return self._config

    @config.setter
    def config(self, value):
        self._config = value

    @staticmethod
    def get_configuration_handler() -> ConfigurationHandlerType:
        if AbstractConfigurationHandler._shared_configuration_handler is None:
            AbstractConfigurationHandler._shared_configuration_handler = AbstractConfigurationHandler()
        return AbstractConfigurationHandler._shared_configuration_handler
