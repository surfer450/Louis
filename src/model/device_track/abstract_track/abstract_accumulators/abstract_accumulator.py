from abc import ABC, abstractmethod
from typing import Any


class Accumulator(ABC):

    def __init__(self, accumulate_point, config):

        self.accumulate_point = accumulate_point
        self.config = config

    @abstractmethod
    def insert_data(self, data: Any) -> None:

        pass

    @abstractmethod
    def is_insertion_legal(self, data: Any) -> bool:

        pass

    @abstractmethod
    def is_retrieval_legal(self) -> bool:

        pass

    @abstractmethod
    def __next__(self):
        pass

    @abstractmethod
    def __iter__(self):
        pass


