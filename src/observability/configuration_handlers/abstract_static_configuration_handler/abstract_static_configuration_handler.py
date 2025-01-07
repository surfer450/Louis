from src.observability.configuration_handlers.abstract_configuration_handler import AbstractConfigurationHandler, \
    ConfigurationHandlerType


class AbstractStaticConfigurationHandler(AbstractConfigurationHandler):
    """
    AbstractStaticConfigurationHandler is a subclass of AbstractConfigurationHandler that manages
    static configuration handling. It is responsible for retrieving and updating the configuration handler
    for a given class.

    Inherits from:
        AbstractConfigurationHandler: The base class for all configuration handlers.
    """

    @classmethod
    def get_configuration_handler(cls) -> ConfigurationHandlerType:
        """
        Retrieves the configuration handler for the class. If it has not been set,
        it invokes the update_config_handler method to set it.

        Args:
            cls: The class invoking this method. It should be a subclass of AbstractStaticConfigurationHandler.

        Returns:
            ConfigurationHandlerType: The configuration handler instance for the class.
        """
        if cls.config_handler is None:
            cls.update_config_handler()
        return cls.config_handler
