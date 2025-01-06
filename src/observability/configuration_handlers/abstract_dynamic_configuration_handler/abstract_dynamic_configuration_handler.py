from src.observability.configuration_handlers.abstract_configuration_handler import AbstractConfigurationHandler, \
    ConfigurationHandlerType


class AbstractDynamicConfigurationHandler(AbstractConfigurationHandler):
    @staticmethod
    def get_configuration_handler() -> ConfigurationHandlerType:
        AbstractDynamicConfigurationHandler.update_config_handler()
        return AbstractDynamicConfigurationHandler.config_handler
