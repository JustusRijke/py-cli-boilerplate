from importlib.metadata import version
from typing import Optional

from .cli import cli

__version__ = version("pycliboilerplate")


def invoke(args: Optional[list[str]] = None) -> None:  # pragma: no cover
    if args is None:
        cli()
    else:
        cli(args, standalone_mode=False)


__all__ = ["invoke", "__version__"]
