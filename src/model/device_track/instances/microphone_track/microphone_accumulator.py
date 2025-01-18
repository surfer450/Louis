from time import time
from typing import Any
from src.model.device_track.abstract_track.abstract_accumulators.abstract_list_accumulator import ListAccumulator


class MicrophoneAccumulator(ListAccumulator):
    """
    A concrete implementation of the ListAccumulator that manages microphone data.
    This class extends the ListAccumulator by adding functionality to track the
    timestamp of the most recent data insertion.
    """

    def __init__(self):
        """
        Initialize the MicrophoneAccumulator with an empty list and no timestamp for the last insertion.
        """
        super().__init__()
        self.last_insertion_timestamp = None

    def update_metadata_in_insertion(self) -> None:
        """
        Update the metadata after data insertion by recording the current timestamp.
        """
        self.last_insertion_timestamp = time()

    def pull_metadata(self) -> time:
        """
        Retrieve the timestamp of the most recent data insertion.

        Returns:
            float: The Unix timestamp of the last data insertion, or `None` if no data has been inserted.
        """
        return self.last_insertion_timestamp
