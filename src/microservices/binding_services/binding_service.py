from queue import Queue

from src.microservices.binding_services.absract_binding_package.abstract_device import Device
from src.microservices.binding_services.absract_binding_package.abstract_driver import Driver
from src.shared_logic.message_broker.exchanges.exchange_type import ExchangeType
from src.shared_logic.message_broker.message_broker import MessageBroker


class BindingService:
    def __init__(self, device: Device, driver: Driver):
        self.device = device
        self.internal_input_queue = Queue()
        self.driver = driver

    def activate_binding(self):
        output_exchange = MessageBroker.declare_exchange("ExchangeBindingsOut", ExchangeType.FANOUT)
        output_queue = MessageBroker.declare_queue("QueueProcessorOut")
        output_exchange.bind_queue("/", output_queue.name)
        self.device.start_device_recording(self.internal_input_queue)
        self.driver.start_driver_action(self.internal_input_queue, output_exchange)
