# exchange_factory.py
import threading
from typing import Dict

from src.shared_logic.message_broker.exceptions.broker_exceptions import ExchangeNotExists, ExchangeAlreadyExists
from src.shared_logic.message_broker.exchanges.base_exchange import BaseExchange
from src.shared_logic.message_broker.exchanges.exchange_type import ExchangeType


class ExchangeFactory:
    _lock = threading.Lock()
    _exchanges: Dict[str, BaseExchange] = {}

    @staticmethod
    def is_exchange_exists(name: str) -> bool:
        return name in ExchangeFactory._exchanges.keys()

    @staticmethod
    def get_exchange(name: str) -> BaseExchange:
        with ExchangeFactory._lock:
            if not ExchangeFactory.is_exchange_exists(name):
                raise ExchangeNotExists(name)

            exchange = ExchangeFactory._exchanges.get(name)
            return exchange

    @staticmethod
    def create_exchange(name: str, exchange_type: ExchangeType) -> BaseExchange:
        with ExchangeFactory._lock:
            if ExchangeFactory.is_exchange_exists(name):
                raise ExchangeAlreadyExists(name)

            exchange = exchange_type.value(name)
            ExchangeFactory._exchanges[name] = exchange
            return exchange
