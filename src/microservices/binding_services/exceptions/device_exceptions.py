class DeviceException(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class DeviceWontStartException(DeviceException):
    def __init__(self, device_name: str, failure_reason: str):
        message = f"The '{device_name}' won't start: {failure_reason}"
        super().__init__(message)


class DeviceWontCloseException(DeviceException):
    def __init__(self, device_name: str, failure_reason: str):
        message = f"The '{device_name}' won't close: {failure_reason}"
        super().__init__(message)


class DeviceNoOutputException(DeviceException):
    def __init__(self, device_name: str, failure_reason: str):
        message = f"The '{device_name}' is recording but couldn't get output data: {failure_reason}"
        super().__init__(message)
