from abc import abstractmethod
from typing import Any
from src.shared_logic.abstract_accumulators.abstract_accumulator import Accumulator


class ListAccumulator(Accumulator):
    """
    A concrete implementation of the Accumulator class that uses a list as the accumulation point.
    This class provides logic for appending data to a list and iterating through its elements.
    """

    def __init__(self):
        """
        Initialize the ListAccumulator with an empty list as the accumulate point.
        """
        super().__init__(accumulate_point=[])

    def __next__(self):
        """
        Retrieve the next element in the list during iteration.

        Raises:
            StopIteration: If there are no more elements to iterate through.

        Returns:
            Any: The next element in the list.
        """
        if self.index >= len(self.accumulate_point):
            raise StopIteration
        item = self.accumulate_point[self.index]
        self.index += 1
        return item

    def insert_data(self, data: Any) -> None:
        """
        Append the provided data to the list.

        Args:
            data (Any): The data to be appended to the list.
        """
        self.accumulate_point.append(data)