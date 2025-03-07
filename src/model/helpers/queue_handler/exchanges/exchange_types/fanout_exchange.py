# fanout_exchange.py
from typing import Any, Optional

from src.model.helpers.queue_handler.exchanges.base_exchange import BaseExchange
from src.model.helpers.queue_handler.factories.queue_factory import QueueFactory


class FanoutExchange(BaseExchange):
    def __init__(self, name: str):
        super().__init__(name)

    def publish(self, message: Any, routing_key: Optional[str] = None) -> None:
        with self._lock:
            bindings_snapshot = list(self.bindings.keys())
        for queue_name in bindings_snapshot:
            QueueFactory.get_queue(queue_name).enqueue(message)
