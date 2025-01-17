from abc import ABC, abstractmethod
from typing import Any

from src.model.device_track.abstract_track.abstract_accumulators.abstract_accumulator import Accumulator


class ListAccumulator(Accumulator):

    def __init__(self, config):

        super().__init__([], config)
        self.index = 0

    def insert_data(self, data: Any) -> None:
        self.accumulate_point.append(data)

    @abstractmethod
    def is_retrieval_legal(self) -> bool:
        pass

    @abstractmethod
    def is_insertion_legal(self, data: Any) -> bool:
        pass

    def __next__(self):
        if self.index < len(self.accumulate_point):
            item = self.accumulate_point[self.index]
            self.index += 1
            return item
        raise StopIteration

    def __iter__(self):
        self.index = 0
        return self
