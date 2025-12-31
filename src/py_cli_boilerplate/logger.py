import logging

LOG_FORMAT = (
    "%(asctime)s %(levelname)-8s %(filename)s:%(lineno)d (%(funcName)s): %(message)s"
)
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


def setup_logging(verbosity: int, save_log: bool) -> logging.Logger:
    if verbosity == 0:
        level = logging.WARNING
    elif verbosity == 1:
        level = logging.INFO
    else:
        level = logging.DEBUG

    formatter = logging.Formatter(LOG_FORMAT, datefmt=DATE_FORMAT)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger = logging.getLogger()
    logger.setLevel(level)
    logger.addHandler(console_handler)

    if save_log:
        file_formatter = logging.Formatter(LOG_FORMAT, datefmt=DATE_FORMAT)
        file_handler = logging.FileHandler("log.txt")
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)

    return logger
