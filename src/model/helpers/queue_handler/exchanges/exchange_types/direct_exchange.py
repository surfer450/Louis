from typing import Any, Optional

from src.model.helpers.queue_handler.exchanges.base_exchange import BaseExchange
from src.model.helpers.queue_handler.factories.queue_factory import QueueFactory


class DirectExchange(BaseExchange):
    def __init__(self, name: str):
        super().__init__(name)

    def publish(self, message: Any, routing_key: Optional[str] = None) -> None:
        with self._lock:
            bindings_snapshot = self.bindings.copy()
        for queue_name, binding_key in bindings_snapshot.items():
            if binding_key == routing_key:
                QueueFactory.get_queue(queue_name).enqueue(message)
