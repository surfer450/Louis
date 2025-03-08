from enum import Enum

from src.shared_logic.queue_handler.exchanges.exchange_types.direct_exchange import DirectExchange
from src.shared_logic.queue_handler.exchanges.exchange_types.fanout_exchange import FanoutExchange
from src.shared_logic.queue_handler.exchanges.exchange_types.topic_exchange import TopicExchange


class ExchangeType(Enum):
    FANOUT = FanoutExchange
    DIRECT = DirectExchange
    TOPIC = TopicExchange
