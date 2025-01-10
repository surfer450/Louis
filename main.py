import cv2

from src.model.devices.instances.camera.camera import Camera
from src.model.devices.instances.microphone.microphone import Microphone
from src.observability.configuration_handlers.instances.devices.camera.camera_device_configuration_handler import \
    CameraDeviceConfigurationHandler
from src.observability.configuration_handlers.instances.devices.microphone.microphone_device_configuration_handler import \
    MicrophoneDeviceConfigurationHandler
from src.observability.logging_handler.instances.basic_logging_handler import BasicLoggingHandler
from pyaudio import PyAudio, paInt16


def main():
    mic = Microphone(0, MicrophoneDeviceConfigurationHandler, BasicLoggingHandler)
    mic.start_device_recording()
    cam = Camera(0, MicrophoneDeviceConfigurationHandler, BasicLoggingHandler)
    cam.start_device_recording()
    while True:
        print(mic.device_recording_logic()[1])
        cv2.imshow("Frame", mic.start_device_recording())


if __name__ == '__main__':
    main()
