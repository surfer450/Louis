class DeviceException(Exception):
    """
    Base exception class for device-related errors.

    This exception serves as the parent class for all device-specific exceptions,
    allowing for consistent error handling across different types of devices.
    """

    def __init__(self, message: str):
        """
        Initializes the DeviceException with a specific error message.

        Args:
            message (str): A descriptive error message for the exception.
        """
        super().__init__(message)


class DeviceOpenException(DeviceException):
    """
    Raised when a device cannot be opened for operation.
    """

    def __init__(self, device_name: str):
        message = f"Failed to open the device '{device_name}'."
        super().__init__(message)


class DeviceDisconnectedException(DeviceException):
    """
    Raised when a device is unexpectedly disconnected during operation.
    """

    def __init__(self, device_name: str):
        message = f"The device '{device_name}' was unexpectedly disconnected."
        super().__init__(message)


class DeviceNotRecordingException(DeviceException):
    """
    Raised when a device is unexpectedly not recording.
    """

    def __init__(self, device_name: str):
        message = f"The device '{device_name}' is not recording"
        super().__init__(message)


class DeviceNoOutputException(DeviceException):
    """
    Raised when a device is recording but nothing is captured.
    """

    def __init__(self, device_name: str, content_name: str):
        message = f"The device '{device_name}' is recording but no {content_name}s are read"
        super().__init__(message)
