import cv2
from src.model.device_track.instances.camera_track.camera import Camera
from src.model.device_track.instances.microphone_track.microphone import Microphone
from src.observability.configuration_handlers.instances.camera_device_configuration_handler import \
    CameraDeviceConfigurationHandler
from src.observability.configuration_handlers.instances.microphone_device_configuration_handler import \
    MicrophoneDeviceConfigurationHandler
from src.observability.logging_handler.instances.basic_logging_handler import BasicLoggingHandler


def main():
    mic = Microphone(0)
    mic.start_device_recording()

    cam = Camera(0)
    cam.start_device_recording()

    while True:
        sound, volume = mic.device_recording_logic()
        print(f"volume: {volume}, sound: {sound}")

        cv2.imshow("Frame", cam.device_recording_logic())
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


if __name__ == '__main__':
    main()
