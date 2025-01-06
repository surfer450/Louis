from json import loads

from src.observability.configuration_handlers.abstract_configuration_handler import AbstractConfigurationHandler, \
    ConfigurationHandlerType
from src.observability.configuration_handlers.shared_logic.helpers.configuration_reader import ConfigurationReader


class AbstractDynamicConfigurationHandler(AbstractConfigurationHandler):
    @staticmethod
    def get_configuration_handler() -> ConfigurationHandlerType:
        AbstractDynamicConfigurationHandler._config_handler = loads(
            ConfigurationReader.read_configfile(AbstractDynamicConfigurationHandler.config_file_path))
        return AbstractDynamicConfigurationHandler._config_handler
