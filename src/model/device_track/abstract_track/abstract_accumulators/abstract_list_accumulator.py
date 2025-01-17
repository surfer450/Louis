from abc import abstractmethod
from typing import Any
from src.model.device_track.abstract_track.abstract_accumulators.abstract_accumulator import Accumulator


class ListAccumulator(Accumulator):
    """
    A concrete implementation of the `Accumulator` class that uses a list to accumulate data.

    This class provides the functionality of accumulating data into a list, iterating over it,
    and checking whether insertion and retrieval operations are legal.
    """

    def __init__(self, config):
        """
        Initializes the ListAccumulator with an empty list and configuration settings.

        Args:
            config (Any): Configuration settings to control the behavior of the accumulator.
        """
        super().__init__([], config)

    def __next__(self):
        """
        Retrieves the next item from the accumulated list. If there are no more items,
        a StopIteration exception is raised.

        Returns:
            Any: The next item in the accumulation point (list).

        Raises:
            StopIteration: If there are no more items in the list to retrieve.
        """
        if self.index >= len(self.accumulate_point):
            raise StopIteration
        item = self.accumulate_point[self.index]
        self.index += 1
        return item

    @abstractmethod
    def insert_data(self, data: Any) -> None:
        """
        Abstract method to insert new data into the accumulated list. Should be implemented by subclasses.

        Args:
            data (Any): The data to be inserted into the list.

        Raises:
            ValueError: If the data insertion is not allowed (based on legality checks).
        """
        pass

    @abstractmethod
    def is_retrieval_legal(self) -> bool:
        """
        Abstract method to determine if data retrieval from the list is allowed.
        Should be implemented by subclasses.

        Returns:
            bool: True if data retrieval is allowed, otherwise False.
        """
        pass
