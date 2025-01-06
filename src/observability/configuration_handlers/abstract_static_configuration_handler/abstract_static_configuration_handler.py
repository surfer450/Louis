from src.observability.configuration_handlers.abstract_configuration_handler import AbstractConfigurationHandler, \
    ConfigurationHandlerType


class AbstractStaticConfigurationHandler(AbstractConfigurationHandler):
    @staticmethod
    def get_configuration_handler() -> ConfigurationHandlerType:
        if AbstractStaticConfigurationHandler.config_handler is None:
            AbstractStaticConfigurationHandler.update_config_handler()
        return AbstractStaticConfigurationHandler.config_handler
