from threading import Thread

from src.microservices.binding_services.absract_binding_package.abstract_device import Device
from src.microservices.binding_services.absract_binding_package.abstract_driver import Driver
from src.microservices.binding_services.binding_service import BindingService
from src.microservices.binding_services.bindings_packages_instances.camera_binding_package.camera import Camera
from src.microservices.binding_services.bindings_packages_instances.camera_binding_package.camera_driver import \
    CameraDriver
from src.microservices.binding_services.bindings_packages_instances.microphone_binding_package.microphone import \
    Microphone
from src.microservices.binding_services.bindings_packages_instances.microphone_binding_package.microphone_driver import \
    MicrophoneDriver
from src.observability.configuration_handlers.instances.camera_device_configuration_handler import \
    CameraDeviceConfigurationHandler
from src.observability.configuration_handlers.instances.microphone_device_configuration_handler import \
    MicrophoneDeviceConfigurationHandler
from src.shared_logic.message_broker.message_broker import MessageBroker


def main():
    Thread(
        target=BindingService(
            device=Microphone(
                MicrophoneDeviceConfigurationHandler.get_configuration_handler().config["default_microphone_index"],
                MicrophoneDeviceConfigurationHandler.get_configuration_handler().config["rate"],
                MicrophoneDeviceConfigurationHandler.get_configuration_handler().config["audio_chunk"]
            ),
            driver=MicrophoneDriver(
                MicrophoneDeviceConfigurationHandler.get_configuration_handler().config["volume_threshold"],
                MicrophoneDeviceConfigurationHandler.get_configuration_handler().config["silence_time_threshold"]
            )
        ).activate_binding
    ).start()

    Thread(
        target=BindingService(
            device=Camera(
                CameraDeviceConfigurationHandler.get_configuration_handler().config["camera_default_index"]
            ),
            driver=CameraDriver(
                CameraDeviceConfigurationHandler.get_configuration_handler().config["brightness_threshold"],
                CameraDeviceConfigurationHandler.get_configuration_handler().config["standard_deviation_threshold"],
                CameraDeviceConfigurationHandler.get_configuration_handler().config["amount_of_legal_frames"]
            )
        ).activate_binding
    ).start()

    output_queue = MessageBroker.declare_queue("QueueProcessorOut")
    while True:
        for a in output_queue.dequeue():
            print(a)


if __name__ == '__main__':
    main()
