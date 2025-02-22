from abc import ABC, abstractmethod
import threading
from typing import Any, Dict, Optional

from src.model.helpers.queue_handler.queues.queue_instance import QueueInstance


class BaseExchange(ABC):
    def __init__(self, name: str):
        self.name = name
        self._lock = threading.Lock()
        self.bindings: Dict[str, Optional[str]] = {}

    def bind_queue(self, key: Optional[str], queue_instance: QueueInstance) -> None:
        """
        Thread-safe binding method.
        :param key: The routing key or pattern. For fanout exchanges, this can be None.
        :param queue_instance: The queue instance to bind.
        """
        with self._lock:
            self.bindings[queue_instance.name] = key

    def unbind_queue(self, key: Optional[str], queue_instance: QueueInstance) -> None:
        """
        Thread-safe unbinding method.
        :param key: The routing key or pattern. For fanout exchanges, this can be None.
        :param queue_instance: The queue instance to unbind.
        """
        with self._lock:
            if queue_instance.name in self.bindings and self.bindings[queue_instance.name] == key:
                del self.bindings[queue_instance.name]

    @abstractmethod
    def publish(self, message: Any, routing_key: Optional[str] = None) -> None:
        """
        Abstract publish method.
        """
        pass
