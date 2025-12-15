import sys

import click

from .logger import setup_logging


@click.command()
@click.argument("foobar", type=str)
@click.option(
    "-v",
    "--verbose",
    "verbosity",
    count=True,
    help="Increase verbosity (-v for INFO, -vv for DEBUG)",
)
@click.option("--save-log", is_flag=True, help="Write log output to log.txt")
@click.version_option(package_name="pycliboilerplate")
def cli(foobar, verbosity, save_log):
    """FOOBAR is an example argument, it's value is printed to stdout"""
    logger = setup_logging(verbosity, save_log)
    logger.debug("Debug logging enabled")

    # Actual program logic goes here
    logger.info("pycliboilerplate started")

    try:
        # Example logic, enclosed in try/except to demonstrate critical error logging
        print(foobar)
    except Exception as e:  # pragma: no cover
        logger.critical(f"Error: {e}", exc_info=True)
        sys.exit(2)

    logger.info("pycliboilerplate finished")
