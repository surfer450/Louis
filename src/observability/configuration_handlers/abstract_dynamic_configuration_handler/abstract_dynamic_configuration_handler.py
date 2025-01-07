from src.observability.configuration_handlers.abstract_configuration_handler import AbstractConfigurationHandler, \
    ConfigurationHandlerType


class AbstractDynamicConfigurationHandler(AbstractConfigurationHandler):
    """
    AbstractDynamicConfigurationHandler is a subclass of AbstractConfigurationHandler designed
    for handling dynamic configuration management. Unlike static configuration handlers, this class
    always updates the configuration handler when `get_configuration_handler` is called.

    Inherits from:
        AbstractConfigurationHandler: The base class that provides the interface for configuration handling.
    """

    @classmethod
    def get_configuration_handler(cls) -> ConfigurationHandlerType:
        """
        Retrieves and updates the configuration handler for the class by calling the `update_config_handler`
        method to ensure the handler is always refreshed before being returned.

        Args:
            cls: The class invoking this method.

        Returns:
            ConfigurationHandlerType: The updated configuration handler instance.
        """
        cls.update_config_handler()
        return cls.config_handler
