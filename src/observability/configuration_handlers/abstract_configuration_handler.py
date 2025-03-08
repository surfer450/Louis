from abc import ABC, abstractmethod
from json import loads, dumps
from threading import Lock
from typing import TypeVar, Dict
from src.shared_logic.IO_handlers.file_handler import FileHandler

ConfigurationHandlerType = TypeVar("ConfigurationHandlerType")


class AbstractConfigurationHandler(ABC):
    """
    An abstract base class for handling configuration files. This class provides methods for
    retrieving, updating, and changing configuration, as well as ensuring thread-safety using locks.

    Subclasses must implement the method to provide the path to the configuration file.
    """
    shared_config = None

    def __init__(self):
        """
        Initializes the configuration handler, retrieves the current configuration, and sets up
        a lock to ensure thread-safe operations.
        """
        self._lock = Lock()
        self._config = self.retrieve_config()


    @property
    def lock(self) -> Lock:
        """
        Gets the current lock object.

        Returns:
            Lock: The current Lock object used for thread-safety.
        """
        return self._lock

    @lock.setter
    def lock(self, lock: Lock) -> None:
        """
        Sets a new lock object for thread-safety.

        Args:
            lock (Lock): The new Lock object to be assigned.
        """
        self._lock = lock

    @property
    def config(self) -> Dict:
        """
        Retrieves the current configuration.

        Returns:
            Dict: The current configuration.
        """
        return self._config

    @config.setter
    def config(self, value: Dict) -> None:
        """
        Sets a new configuration.

        Args:
            value (Dict): The new configuration to be set.
        """
        self._config = value

    @abstractmethod
    def get_config_path(self) -> str:
        """
        Abstract method to retrieve the path to the configuration file.

        Returns:
            str: The path to the configuration file.
        """
        pass

    def retrieve_config(self) -> Dict:
        """
        Retrieves the configuration by reading the file specified by the subclass's
        `get_config_path` method. Ensures thread-safety using a lock.

        Returns:
            Dict: The configuration data as a dictionary.
        """
        with self.lock:
            return loads(FileHandler.read_file(self.get_config_path()))

    def update_config(self) -> None:
        """
        Updates the current configuration by retrieving the latest configuration from the file.
        Ensures thread-safety using a lock.
        """
        with self.lock:
            self.config = self.retrieve_config()

    def change_config(self, config: Dict) -> None:
        """
        Changes the current configuration and writes the updated configuration to the file.
        Ensures thread-safety using a lock.

        Args:
            config (Dict): The new configuration to be written to the file.
        """
        with self.lock:
            self.config = config
            FileHandler.write_file(self.get_config_path(), dumps(config))

    @classmethod
    def get_configuration_handler(cls) -> ConfigurationHandlerType:
        """
        Retrieves the singleton instance of the configuration handler. If no instance exists,
        a new one is created.

        Returns:
            ConfigurationHandlerType: The singleton instance of the configuration handler.
        """
        if cls.shared_config is None:
            cls.shared_config = cls()
        return cls.shared_config
