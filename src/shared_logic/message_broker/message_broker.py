from src.shared_logic.message_broker.exceptions.broker_exceptions import QueueAlreadyExists, ExchangeAlreadyExists, \
    IncorrectExchangeType
from src.shared_logic.message_broker.exchanges.base_exchange import BaseExchange
from src.shared_logic.message_broker.factories.queue_factory import QueueFactory
from src.shared_logic.message_broker.factories.exchange_factory import ExchangeFactory
from src.shared_logic.message_broker.exchanges.exchange_type import ExchangeType


class MessageBroker:
    @staticmethod
    def declare_queue(name: str):
        """
        Create (or retrieve an existing) queue.
        """
        try:
            return QueueFactory.create_queue(name)

        except QueueAlreadyExists:
            return QueueFactory.get_queue(name)

    @staticmethod
    def declare_exchange(name: str, exchange_type: ExchangeType) -> BaseExchange:
        """
        Create (or retrieve an existing) exchange of the given type.
        """
        try:
            return ExchangeFactory.create_exchange(name, exchange_type)

        except ExchangeAlreadyExists:
            exchange = ExchangeFactory.get_exchange(name)

            if not isinstance(exchange, exchange_type.value):
                raise IncorrectExchangeType(exchange.name, exchange_type.name, type(exchange).__name__)

            return ExchangeFactory.get_exchange(name)
