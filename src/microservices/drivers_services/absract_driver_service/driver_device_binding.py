from queue import Queue

from src.microservices.drivers_services.absract_driver_service.abstract_device import Device
from src.microservices.drivers_services.absract_driver_service.abstract_driver import Driver


class DriverDeviceBending:
    def __init__(self, device: Device, driver: Driver):
        self.device = device
        self.input_queue = Queue()
        self.driver = driver
        self.output_queue = Queue()

    def activate_binding(self):
        self.device.start_device_recording(self.input_queue)
        self.driver.start_driver_action(self.input_queue, self.output_queue)

        while True:
            command = self.output_queue.get()
            for data in command:
                print(data)
