import cv2
from src.model.device_track.instances.camera_track.camera import Camera
from src.model.device_track.instances.microphone_track.microphone import Microphone
from src.model.device_track.instances.microphone_track.microphone_accumulator import MicrophoneAccumulator
from src.observability.configuration_handlers.instances.camera_device_configuration_handler import \
    CameraDeviceConfigurationHandler
from src.observability.configuration_handlers.instances.microphone_device_configuration_handler import \
    MicrophoneDeviceConfigurationHandler
from src.observability.logging_handler.instances.basic_logging_handler import BasicLoggingHandler


def main():
    mic = Microphone(0)
    mic.start_device_recording()
    mic_accumulator = MicrophoneAccumulator()

    while mic_accumulator.is_retrieval_legal() is not True:
        sound, volume = mic.device_recording_logic()
        print(volume)
        mic_accumulator.insert_data(sound)

    for data in mic_accumulator:
        print(data)




if __name__ == '__main__':
    main()
