from abc import ABC, abstractmethod
from typing import Any

class Accumulator(ABC):
    """
    Abstract base class for an Accumulator, which defines a structure for accumulating,
    storing, and retrieving data. Subclasses must implement the specified methods to
    define custom behavior for data insertion and retrieval.
    """

    def __init__(self):
        """
        Initializes the Accumulator with a default `accumulate_point` set to None.
        This can be used by subclasses to track the state of the accumulator.
        """
        self.accumulate_point = None

    @abstractmethod
    def is_insertion_legal(self, data: Any) -> bool:
        """
        Determines whether inserting the given data into the accumulator is allowed.

        Args:
            data (Any): The data to be checked for insertion legality.

        Returns:
            bool: True if the insertion is legal, False otherwise.
        """
        pass

    @abstractmethod
    def insert_data(self, data: Any) -> None:
        """
        Inserts the given data into the accumulator if it is legal to do so.

        Args:
            data (Any): The data to be inserted.

        Raises:
            Exception: If the insertion is not legal or fails due to subclass-specific rules.
        """
        pass

    @abstractmethod
    def is_retrieval_legal(self) -> bool:
        """
        Determines whether it is currently legal to retrieve data from the accumulator.

        Returns:
            bool: True if data can be retrieved, False otherwise.
        """
        pass

    @abstractmethod
    def retrieve_data(self) -> Any:
        """
        Retrieves data from the accumulator if it is legal to do so.

        Returns:
            Any: The retrieved data.

        Raises:
            Exception: If the retrieval is not legal or fails due to subclass-specific rules.
        """
        pass
