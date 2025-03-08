from typing import Any, Optional
import re

from src.shared_logic.queue_handler.exchanges.base_exchange import BaseExchange
from src.shared_logic.queue_handler.factories.queue_factory import QueueFactory


class TopicExchange(BaseExchange):
    def __init__(self, name: str):
        super().__init__(name)

    def publish(self, message: Any, routing_key: Optional[str] = None) -> None:
        with self._lock:
            bindings_snapshot = self.bindings.copy()
        for queue_name, pattern in bindings_snapshot.items():
            if self._match(pattern, routing_key):
                QueueFactory.get_queue(queue_name).enqueue(message)

    @staticmethod
    def _match(pattern: str, routing_key: Optional[str]) -> bool:
        if routing_key is None:
            return False
        regex_pattern = re.escape(pattern)
        regex_pattern = regex_pattern.replace(r'\*', '[^.]+')
        regex_pattern = regex_pattern.replace(r'\#', '.*')
        regex_pattern = '^' + regex_pattern + '$'
        return re.match(regex_pattern, routing_key) is not None
