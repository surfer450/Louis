# broker.py
import threading
from typing import Any, Optional

from src.model.helpers.queue_handler.factories.queue_factory import QueueFactory
from src.model.helpers.queue_handler.factories.exchange_factory import ExchangeFactory
from src.model.helpers.queue_handler.exchanges.exchange_type import ExchangeType


class MessageBroker:
    @staticmethod
    def create_queue(name: str):
        """
        Create (or retrieve an existing) queue.
        """
        return QueueFactory.get_queue(name)

    @staticmethod
    def create_exchange(name: str, exchange_type: ExchangeType):
        """
        Create (or retrieve an existing) exchange of the given type.
        """
        return ExchangeFactory.get_exchange(name, exchange_type)

    @staticmethod
    def bind_queue(exchange_name: str, queue_name: str, routing_key: Optional[str] = None):
        """
        Bind a queue to an exchange with the specified routing key.
        Assumes the exchange has been created (or will be created as a default type if needed).
        """
        queue = QueueFactory.get_queue(queue_name)
        exchange = ExchangeFactory.get_exchange(exchange_name, ExchangeType.DIRECT)
        exchange.bind_queue(routing_key, queue)

    @staticmethod
    def publish(exchange_name: str, message: Any, routing_key: Optional[str] = None):
        """
        Publish a message to an exchange. The exchange will route the message to bound queues.
        """
        exchange = ExchangeFactory.get_exchange(exchange_name, ExchangeType.DIRECT)
        exchange.publish(message, routing_key)

    @staticmethod
    def read_message(queue_name: str) -> None:
        queue_instance = QueueFactory.get_queue(queue_name)
        return queue_instance.dequeue()
