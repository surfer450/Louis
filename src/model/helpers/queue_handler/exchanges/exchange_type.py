from enum import Enum

from src.model.helpers.queue_handler.exchanges.exchange_types.direct_exchange import DirectExchange
from src.model.helpers.queue_handler.exchanges.exchange_types.fanout_exchange import FanoutExchange
from src.model.helpers.queue_handler.exchanges.exchange_types.topic_exchange import TopicExchange


class ExchangeType(Enum):
    FANOUT = FanoutExchange
    DIRECT = DirectExchange
    TOPIC = TopicExchange