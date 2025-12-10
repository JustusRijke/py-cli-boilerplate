from .cli import cli


def main(args=None):
    if args is None:
        cli()
    else:
        cli(args, standalone_mode=False)


__all__ = ["main"]
