from src.observability.logging_handler.instances.basic_logging_handler import LoggerHandler


def main():
    set_logger()


def set_logger():
    logger_handler = LoggerHandler.get_logger_handler()
    logger = logger_handler.logger
    logger.info("Logger initialized successfully")


if __name__ == '__main__':
    main()
