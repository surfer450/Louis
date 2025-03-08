from abc import ABC, abstractmethod
from typing import Any

class Accumulator(ABC):
    """
    Abstract base class for an Accumulator that manages and processes data.
    This class provides a framework for defining accumulators with customizable data insertion
    logic, metadata management, and iteration behavior.
    """

    def __init__(self, accumulate_point: Any):
        """
        Initialize the Accumulator with a specified accumulate point.

        Args:
            accumulate_point (Any): A value that defines the accumulation criteria
                                    or point of operation for the accumulator.
        """
        self.accumulate_point = accumulate_point
        self.index = 0

    def __iter__(self):
        """
        Reset and return the iterator for the Accumulator.

        Returns:
            Accumulator: The iterator instance itself.
        """
        self.index = 0
        return self

    @abstractmethod
    def __next__(self):
        """
        Define the logic for retrieving the next item in the accumulation process.

        Raises:
            StopIteration: When there are no more items to iterate over.

        Returns:
            Any: The next item in the sequence.
        """
        pass

    @abstractmethod
    def insert_data(self, data: Any) -> None:
        """
        Insert data into the Accumulator and update its metadata.

        Args:
            data (Any): The data to be inserted into the Accumulator.
        """
