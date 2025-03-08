import time
import numpy
from src.microservices.binding_services.absract_binding_package.abstract_driver import Driver
from src.microservices.binding_services.bindings_packages_instances.microphone_binding_package.voice_helper import VoiceHelper
from src.shared_logic.accumulators.list_accumulator import ListAccumulator


class MicrophoneDriver(Driver):
    def __init__(self, volume_threshold: int,
                 silence_time_threshold: int):
        super().__init__(ListAccumulator())
        self.last_insertion_time = None
        self.volume_threshold = volume_threshold
        self.silence_time_threshold = silence_time_threshold

    def is_input_data_valid(self, data: numpy.ndarray[numpy.float32]) -> bool:
        volume = VoiceHelper.get_voice_volume(data)
        if volume < self.volume_threshold:
            return False

        return True

    def input_activation(self):
        self.last_insertion_time = time.time()

    def is_output_data_valid(self) -> bool:
        if self.last_insertion_time is None:
            return False

        time_since_last_voice = time.time() - self.last_insertion_time
        if time_since_last_voice < self.silence_time_threshold:
            return False

        return True

    def output_activation(self):
        self.accumulator = ListAccumulator()
        self.last_insertion_time = None
