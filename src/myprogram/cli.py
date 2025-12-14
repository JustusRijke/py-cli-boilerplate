import click

from .logger import setup_logging


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
    logger.debug("Debug logging enabled")

    # Actual program logic goes here
    logger.info("myprogram started")
    if foobar:
        print(foobar)
    logger.info("myprogram finished")
