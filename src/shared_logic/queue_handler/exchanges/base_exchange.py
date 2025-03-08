from abc import ABC, abstractmethod
from threading import Lock
from typing import Any, Dict
from src.shared_logic.queue_handler.exceptions.broker_exceptions import QueueNotExists
from src.shared_logic.queue_handler.factories.queue_factory import QueueFactory


class BaseExchange(ABC):
    def __init__(self, name: str):
        self.name = name
        self._lock = Lock()
        self.bindings: Dict[str, str] = {}

    def bind_queue(self, key: str, queue_instance_name: str) -> None:
        """
        Thread-safe binding method.
        :param key: The routing key or pattern. if binding exists, override it.
        :param queue_instance_name: The queue instance name to bind.
        """
        with self._lock:
            if not QueueFactory.is_queue_exists(queue_instance_name):
                raise QueueNotExists(queue_instance_name)

            self.bindings[queue_instance_name] = key

    def unbind_queue(self, queue_instance_name: str) -> None:
        """
        Thread-safe unbinding method.
        :param queue_instance_name: The queue instance name to unbind. if not in bindings, won't do anything.
        """
        with self._lock:
            if not QueueFactory.is_queue_exists(queue_instance_name):
                raise QueueNotExists(queue_instance_name)

            if queue_instance_name in self.bindings:
                del self.bindings[queue_instance_name]

    @abstractmethod
    def publish(self, message: Any, routing_key: str) -> None:
        """
        Abstract publish method.
        """
        pass
