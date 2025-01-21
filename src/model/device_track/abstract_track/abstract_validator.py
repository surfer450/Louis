from abc import ABC
from typing import Callable, List

from src.model.device_track.instances.shared_logic.helpers.data_context import DataContext


class Validator(ABC):
    DEFAULT_VALIDATORS: List[str] = []

    @classmethod
    def initialize_validators(cls) -> List[Callable]:
        """
        Convert DEFAULT_VALIDATORS (method names) into callable functions.
        :return: List of validation functions.
        :Raises: ValueError for functions that are not implemented within the child class.
        """
        try:
            return [getattr(cls, func_name) for func_name in cls.DEFAULT_VALIDATORS]
        except AttributeError as e:
            raise ValueError(f"Invalid validator name in DEFAULT_VALIDATORS: {e}")

    @classmethod
    def is_valid(cls, context: DataContext, validation_functions: List[Callable] = None) -> bool:
        """
        Validate the context using a list of validation functions.
        :param context: The data context (data and metadata).
        :param validation_functions: A list of validation functions. Defaults to the class's default validators.
        :return: True if all validation functions pass, False otherwise.
        """
        functions = validation_functions or cls.initialize_validators()

        for validate in functions:
            if not validate(context):
                return False
        return True
