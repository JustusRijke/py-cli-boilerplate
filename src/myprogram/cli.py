import logging

import click
import colorlog


def setup_logging(verbosity, save_log):
    if verbosity == 0:
        level = logging.WARNING
    elif verbosity == 1:
        level = logging.INFO
    else:
        level = logging.DEBUG

    formatter = colorlog.ColoredFormatter(
        "%(log_color)s%(asctime)s %(levelname)-8s%(reset)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        log_colors={
            "DEBUG": "cyan",
            "INFO": "green",
            "WARNING": "yellow",
            "ERROR": "red",
            "CRITICAL": "red,bg_white",
        },
    )

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger = logging.getLogger()
    logger.setLevel(level)
    logger.addHandler(console_handler)

    if save_log:
        file_formatter = logging.Formatter(
            "%(asctime)s %(levelname)-8s %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        file_handler = logging.FileHandler("log.txt")
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)

    return logger


@click.command()
@click.option("--foobar", type=str, help="Example argument; prints value to stdout")
@click.option(
    "-v",
    "--verbose",
    "verbosity",
    count=True,
    help="Increase verbosity (-v for INFO, -vv for DEBUG)",
)
@click.option("--save-log", is_flag=True, help="Write log output to log.txt")
@click.version_option(package_name="myprogram")
def cli(foobar, verbosity, save_log):
    logger = setup_logging(verbosity, save_log)

    if foobar:
        print(foobar)

    logger.info("myprogram started")
    logger.debug("Debug logging enabled")
