from abc import ABC, abstractmethod
from typing import Any


class Accumulator(ABC):
    """
    An abstract base class representing an accumulator that processes data and manages an accumulation point.

    This class serves as a blueprint for custom accumulator implementations, where the behavior of accumulating,
    inserting, and retrieving data can be defined by the subclass.
    """

    def __init__(self, accumulate_point: Any, config: Any):
        """
        Initializes an accumulator instance with a starting accumulation point and configuration settings.

        Args:
            accumulate_point (Any): The point where data will be accumulated.
            config (Any): Configuration settings that might influence how the accumulator works.
        """
        self.accumulate_point = accumulate_point
        self.config = config
        self.index = 0

    def __iter__(self):
        """
        Initializes the iterator by resetting the index to 0, allowing iteration from the beginning.

        Returns:
            Accumulator: The current accumulator instance, which is iterable.
        """
        self.index = 0
        return self

    @abstractmethod
    def __next__(self):
        """
        Abstract method to retrieve the next item from the accumulator. Should be implemented by subclasses.

        Returns:
            Any: The next accumulated data item.

        Raises:
            StopIteration: If there are no more items to retrieve.
        """
        pass

    @abstractmethod
    def insert_data(self, data: Any) -> None:
        """
        Abstract method to insert new data into the accumulator. Should be implemented by subclasses.

        Args:
            data (Any): The data to insert into the accumulator.

        Raises:
            ValueError: If data insertion is not allowed (based on legality check).
        """
        pass

    @abstractmethod
    def is_retrieval_legal(self) -> bool:
        """
        Abstract method to check if retrieving data from the accumulator is allowed.
        Should be implemented by subclasses.

        Returns:
            bool: True if retrieval is legal, otherwise False.
        """
        pass