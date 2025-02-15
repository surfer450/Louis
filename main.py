import asyncio
import time
from src.microservices.drivers_services.microphone_driver_service.microphone import Microphone
from src.microservices.drivers_services.microphone_driver_service.microphone_driver import MicrophoneDriver


def main():
    asyncio.run(MicrophoneDriver().activate_driver())


if __name__ == '__main__':
    main()
