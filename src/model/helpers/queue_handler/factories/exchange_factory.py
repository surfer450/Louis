# exchange_factory.py
import threading
from typing import Dict

from src.model.helpers.queue_handler.exchanges.base_exchange import BaseExchange
from src.model.helpers.queue_handler.exchanges.exchange_type import ExchangeType


class ExchangeFactory:
    _lock = threading.Lock()
    _exchanges: Dict[str, BaseExchange] = {}

    @staticmethod
    def get_exchange(name: str, exchange_type: ExchangeType) -> BaseExchange:
        with ExchangeFactory._lock:
            exchange = ExchangeFactory._exchanges.get(name)
            if exchange is not None:
                return exchange

            return ExchangeFactory._create_exchange(name, exchange_type)

    @staticmethod
    def _create_exchange(name: str, exchange_type: ExchangeType) -> BaseExchange:
        exchange = exchange_type.value(name)
        ExchangeFactory._exchanges[name] = exchange
        return exchange
