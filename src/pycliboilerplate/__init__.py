from importlib.metadata import version

from .cli import cli

__version__ = version("pycliboilerplate")


def invoke(args=None):  # pragma: no cover
    if args is None:
        cli()
    else:
        cli(args, standalone_mode=False)


__all__ = ["invoke", "__version__"]
