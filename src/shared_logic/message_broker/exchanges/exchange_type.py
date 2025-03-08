from enum import Enum

from src.shared_logic.message_broker.exchanges.exchange_types.direct_exchange import DirectExchange
from src.shared_logic.message_broker.exchanges.exchange_types.fanout_exchange import FanoutExchange
from src.shared_logic.message_broker.exchanges.exchange_types.topic_exchange import TopicExchange


class ExchangeType(Enum):
    FANOUT = FanoutExchange
    DIRECT = DirectExchange
    TOPIC = TopicExchange
