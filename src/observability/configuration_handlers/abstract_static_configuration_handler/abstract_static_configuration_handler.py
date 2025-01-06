from json import loads

from src.observability.configuration_handlers.abstract_configuration_handler import AbstractConfigurationHandler, \
    ConfigurationHandlerType
from src.observability.configuration_handlers.shared_logic.helpers.configuration_reader import ConfigurationReader


class AbstractStaticConfigurationHandler(AbstractConfigurationHandler):
    @staticmethod
    def get_configuration_handler() -> ConfigurationHandlerType:
        if AbstractStaticConfigurationHandler._config_handler is None:
            AbstractStaticConfigurationHandler._config_handler = loads(
                ConfigurationReader.read_configfile(AbstractStaticConfigurationHandler.config_file_path))
        return AbstractStaticConfigurationHandler._config_handler
