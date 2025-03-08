class BrokerException(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class QueueNotExists(BrokerException):
    def __init__(self, queue_name: str):
        message = f"The queue <'{queue_name}'> doesn't exists"
        super().__init__(message)


class QueueAlreadyExists(BrokerException):
    def __init__(self, queue_name: str):
        message = f"The queue <'{queue_name}'> already exists"
        super().__init__(message)


class ExchangeNotExists(BrokerException):
    def __init__(self, exchange_name: str):
        message = f"The exchange <'{exchange_name}'> doesn't exists"
        super().__init__(message)


class ExchangeAlreadyExists(BrokerException):
    def __init__(self, exchange_name: str):
        message = f"The exchange <'{exchange_name}'> already exists"
        super().__init__(message)


class IncorrectExchangeType(BrokerException):
    def __init__(self, exchange_name: str, incorrect_exchange_type: str, correct_exchange_type: str):
        message = (f"tried declaring exchange <'{exchange_name}'> with type: <{incorrect_exchange_type}>, "
                   f"but exchange exists already with type <{correct_exchange_type}>")
        super().__init__(message)



