# exchange_factory.py
import threading

from src.model.helpers.queue_handler.queues.queue_instance import QueueInstance


class QueueFactory:
    _lock = threading.Lock()

    _queues = {}

    @staticmethod
    def get_queue(name: str) -> QueueInstance:
        with QueueFactory._lock:
            queue = QueueFactory._queues.get(name)
            if queue is not None:
                return queue

            queue = QueueInstance(name)
            QueueFactory._queues[name] = queue
            return queue
