import time
from typing import List
from src.model.device_track.abstract_track.abstract_accumulators.abstract_list_accumulator import ListAccumulator
from src.observability.configuration_handlers.instances.microphone_device_configuration_handler import \
    MicrophoneDeviceConfigurationHandler


class MicrophoneAccumulator(ListAccumulator):
    """
    A concrete implementation of the `ListAccumulator` class, specifically designed for accumulating
    microphone sound data. This class handles the insertion of sound data (as lists of integers), enforces
    certain insertion conditions based on volume, and controls when data retrieval is allowed based on
    elapsed time since the last insertion.
    """

    def __init__(self):
        """
        Initializes the `MicrophoneAccumulator` with configuration settings for the microphone device.
        The configuration is loaded via `MicrophoneDeviceConfigurationHandler`.

        Attributes like `last_insertion_timestamp` are initialized to track the time of data insertions.
        """
        super().__init__(MicrophoneDeviceConfigurationHandler.get_configuration_handler().config)
        self.last_insertion_timestamp = None

    def insert_data(self, sound: List[int]) -> None:
        """
        Inserts new sound data into the accumulator, appends it to the accumulated data list, and
        records the timestamp of the insertion.

        Args:
            sound (List[int]): The microphone sound data (represented as a list of integers) to insert.
        """
        self.accumulate_point.append(sound)
        self.last_insertion_timestamp = time.time()

    def is_retrieval_legal(self) -> bool:
        """
        Checks if enough time has passed since the last data insertion to allow retrieval of accumulated data.

        Returns:
            bool: True if the time since the last insertion exceeds the configured silence time threshold,
                  allowing data retrieval. False otherwise.
        """
        if self.last_insertion_timestamp is not None:
            time_since_last_insertion = time.time() - self.last_insertion_timestamp
            return time_since_last_insertion > self.config["silence_time_threshold"]
        return False
