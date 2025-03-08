import queue
from typing import Any, Optional


class QueueInstance:
    def __init__(self, name: str, maxsize: int = 0):
        self.name = name
        self.queue = queue.Queue(maxsize=maxsize)

    def enqueue(self, message: Any) -> None:
        self.queue.put(message)

    def dequeue(self, block: bool = True, timeout: Optional[float] = None) -> Any:
        return self.queue.get(block=block, timeout=timeout)

    def size(self) -> int:
        return self.queue.qsize()

    def is_empty(self) -> bool:
        return self.queue.empty()
