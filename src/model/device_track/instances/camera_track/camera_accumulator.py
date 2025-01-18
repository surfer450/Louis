from src.model.device_track.abstract_track.abstract_accumulators.abstract_list_accumulator import ListAccumulator


class MicrophoneAccumulator(ListAccumulator):
    """
    A concrete implementation of the ListAccumulator that manages microphone data.
    This class extends the ListAccumulator by keeping track of the total number
    of frames (data insertions) that have occurred.
    """

    def __init__(self):
        """
        Initialize the MicrophoneAccumulator with an empty list and a counter for the number of frames.
        """
        super().__init__()
        self.amount_of_frames = 0

    def update_metadata_in_insertion(self) -> None:
        """
        Update the metadata after data insertion by incrementing the frame count.
        """
        self.amount_of_frames += 1

    def pull_metadata(self) -> int:
        """
        Retrieve the total number of frames (data insertions) recorded.

        Returns:
            int: The total number of frames added to the accumulator.
        """
        return self.amount_of_frames
