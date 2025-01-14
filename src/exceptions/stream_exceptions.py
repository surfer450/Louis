class StreamException(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class StreamWontStartException(StreamException):
    def __init__(self, stream_name: str, failure_reason: str):
        message = f"The '{stream_name}' won't start: {failure_reason}"
        super().__init__(message)


class StreamWontCloseException(StreamException):
    def __init__(self, stream_name: str, failure_reason: str):
        message = f"The '{stream_name}' won't close: {failure_reason}"
        super().__init__(message)


class StreamIsInvalid(StreamException):
    def __init__(self, stream_name: str, failure_reason: str):
        message = f"The '{stream_name}' is invalid: {failure_reason}"
        super().__init__(message)


class StreamNoOutputException(StreamException):
    def __init__(self, stream_name: str, failure_reason: str):
        message = f"The '{stream_name}' is recording but couldn't get output data: {failure_reason}"
        super().__init__(message)
