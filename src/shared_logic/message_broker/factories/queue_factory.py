from threading import Lock
from typing import Dict
from src.shared_logic.message_broker.exceptions.broker_exceptions import QueueNotExists, QueueAlreadyExists
from src.shared_logic.message_broker.queues.queue_instance import QueueInstance


class QueueFactory:
    _lock = Lock()
    _queues: Dict[str, QueueInstance] = {}

    @staticmethod
    def is_queue_exists(name: str) -> bool:
        return name in QueueFactory._queues.keys()

    @staticmethod
    def get_queue(name: str) -> QueueInstance:
        with QueueFactory._lock:
            if not QueueFactory.is_queue_exists(name):
                raise QueueNotExists(name)

            queue = QueueFactory._queues.get(name)
            return queue

    @staticmethod
    def create_queue(name: str) -> QueueInstance:
        with QueueFactory._lock:
            if QueueFactory.is_queue_exists(name):
                raise QueueAlreadyExists(name)

            queue = QueueInstance(name)
            QueueFactory._queues[name] = queue
            return queue
