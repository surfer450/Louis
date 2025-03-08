import numpy
from src.microservices.binding_services.absract_binding_package.abstract_driver import Driver
from src.microservices.binding_services.bindings_packages_instances.camera_binding_package.frame_helper import FrameHelper
from src.shared_logic.accumulators.list_accumulator import ListAccumulator


class CameraDriver(Driver):
    def __init__(self, brightness_threshold: int,
                 standard_deviation_threshold: int, amount_of_legal_frames: int):
        super().__init__(ListAccumulator())
        self.amount_of_frames = 0
        self.brightness_threshold = brightness_threshold
        self.standard_deviation_threshold = standard_deviation_threshold
        self.amount_of_legal_frames = amount_of_legal_frames

    def is_input_data_valid(self, data: numpy.ndarray) -> bool:
        brightness = FrameHelper.get_frame_brightness(data)
        if brightness < self.brightness_threshold:
            return False

        variation = FrameHelper.get_frame_variation(data)
        if variation < self.standard_deviation_threshold:
            return False

        return True

    def input_activation(self):
        self.amount_of_frames += 1

    def is_output_data_valid(self) -> bool:
        return self.amount_of_frames > self.amount_of_legal_frames

    def output_activation(self):
        self.accumulator = ListAccumulator()
        self.amount_of_frames = 0
