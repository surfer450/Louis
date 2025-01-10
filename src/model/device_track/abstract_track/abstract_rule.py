from abc import ABC, abstractmethod
from typing import Any, List


class Rule(ABC):
    """
    Abstract base class for defining rules that process incoming data
    and evaluate conditions based on a specified trigger value.
    """

    def __init__(self, trigger_value: int):
        """
        Initialize the Rule instance with a trigger value and an empty data list.

        Args:
            trigger_value (int): The threshold or condition value that the rule uses for evaluation.
        """
        self.data_list: List[Any] = []
        self.trigger_value = trigger_value

    def add_data(self, data: Any) -> None:
        """
        Add a data item to the internal data list for evaluation.

        Args:
            data (any): The data item to be added (e.g., video frame, audio chunk).
        """
        self.data_list.append(data)

    @abstractmethod
    def evaluate(self) -> bool:
        """
        Evaluates the current state of the internal data list against the trigger value.

        Returns:
            bool: True if the evaluation condition is met according to the internal value of trigger value,
                  False otherwise.
        """
        pass

    def get_device_data(self) -> List[Any]:
        """
        Retrieve the list of stored data items.

        Returns:
            list: The current list of data items.
        """
        return self.data_list

    def set_rule_trigger(self, trigger_value: int) -> None:
        """
        Update the trigger value for the rule.

        Args:
            trigger_value (int): The new threshold or condition value for evaluation.
        """
        self.trigger_value = trigger_value

    @abstractmethod
    def reset(self) -> None:
        """
        Reset the state of the rule by clearing the internal data list.

        This method should also reset any other internal state maintained by
        specific rule implementations.
        """
        self.data_list.clear()

    @abstractmethod
    def get_trigger_description(self) -> str:
        """
        Provide a human-readable description of the trigger condition for this rule.

        Returns:
            str: A description of the rule's trigger condition.
        """
        pass
