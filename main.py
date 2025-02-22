from queue import Queue
from threading import Thread

from src.microservices.drivers_services.absract_driver_service.driver_device_binding import DriverDeviceBending
from src.microservices.drivers_services.camera_driver_service.camera import Camera
from src.microservices.drivers_services.camera_driver_service.camera_driver import CameraDriver
from src.microservices.drivers_services.microphone_driver_service.microphone import Microphone
from src.microservices.drivers_services.microphone_driver_service.microphone_driver import MicrophoneDriver
from src.observability.configuration_handlers.instances.camera_device_configuration_handler import \
    CameraDeviceConfigurationHandler
from src.observability.configuration_handlers.instances.microphone_device_configuration_handler import \
    MicrophoneDeviceConfigurationHandler


def main1():
    mic_config = MicrophoneDeviceConfigurationHandler.get_configuration_handler().config
    mic = Microphone(mic_config["default_microphone_index"],
                     mic_config["rate"],
                     mic_config["audio_chunk"])

    mic_driver = MicrophoneDriver(mic_config["volume_threshold"],
                                  mic_config["silence_time_threshold"])

    driver_device_binding = DriverDeviceBending(mic, mic_driver)
    Thread(target=driver_device_binding.activate_binding).start()


def main2():
    cam_config = CameraDeviceConfigurationHandler.get_configuration_handler().config
    cam = Camera(cam_config["camera_default_index"])
    cam_driver = CameraDriver(cam_config["brightness_threshold"],
                              cam_config["standard_deviation_threshold"], cam_config["amount_of_legal_frames"])

    driver_device_binding = DriverDeviceBending(cam, cam_driver)
    Thread(target=driver_device_binding.activate_binding).start()


if __name__ == '__main__':
    main2()
