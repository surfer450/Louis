from abc import ABC, abstractmethod
from typing import Any, Callable, List


class Validator(ABC):
    DEFAULT_VALIDATORS: List[str] = []

    def __init__(self, validation_functions: List[Callable] = None):
        """
        Initialize the Validator with a list of validation functions.
        If no validation functions are provided, use the default ones.
        """
        self.validation_functions = validation_functions or self.initialize_validators()

    @abstractmethod
    def is_valid(self, raw_data: Any) -> bool:
        """Check if the raw_data is valid."""
        pass

    def initialize_validators(self) -> List[Callable]:
        """
        Convert DEFAULT_VALIDATORS (method names) into callable functions.
        :return: List of validation functions.
        """
        return [getattr(self, func_name) for func_name in self.DEFAULT_VALIDATORS]
