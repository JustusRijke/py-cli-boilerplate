# py-cli-boilerplate

[![Build](https://github.com/JustusRijke/py-cli-boilerplate/actions/workflows/build.yml/badge.svg)](https://github.com/JustusRijke/py-cli-boilerplate/actions/workflows/build.yml)
[![codecov](https://codecov.io/github/JustusRijke/py-cli-boilerplate/graph/badge.svg?token=PXD6VY28LO)](https://codecov.io/github/JustusRijke/py-cli-boilerplate)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A minimal Python CLI boilerplate template for GitHub-hosted projects.

## Usage as Template

1. [Create a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template#creating-a-repository-from-a-template) directly using this template
1. Find and replace `pycliboilerplate` with your desired program name
1. Rename `src/pycliboilerplate/` directory to match your program name
1. Update [pyproject.toml](pyproject.toml) with your project details
1. Update badge URLs in README.md with your repository information

### Optional Setup

- **Enable Dependabot**: Go to Settings > Code security and analysis > Dependabot to enable automatic dependency updates
- **Enable Codecov**: Set up [Codecov](https://codecov.io) integration for code coverage tracking

## Installation

Install the package:
```bash
pip install .
```

Install with dev dependencies (pytest, ruff, mypy):
```bash
pip install -e .[dev]
```

## CLI Usage

```
$pycliboilerplate --help

Usage: pycliboilerplate [OPTIONS] FOOBAR

  FOOBAR is an example argument, it's value is printed to stdout

Options:
  -v, --verbose  Increase verbosity (-v for INFO, -vv for DEBUG)
  --save-log     Write log output to log.txt
  --version      Show the version and exit.
  --help         Show this message and exit.
```

Example:
```bash
$pycliboilerplate "hello world" -vv

2025-12-15 14:14:32 DEBUG    cli.py:22 (cli): Debug logging enabled
2025-12-15 14:14:32 INFO     cli.py:25 (cli): pycliboilerplate started
hello world
2025-12-15 14:14:32 INFO     cli.py:34 (cli): pycliboilerplate finished
```

## Library Usage

Run from Python:
```python
from pycliboilerplate import invoke
invoke(["-vv","hello world"])
```

## Development

Run tests:
```bash
pytest tests/
```

Check code quality:
```bash
ruff check
ruff format --check
mypy --strict .
```

Install pre-commit hook (runs ruff and mypy automatically before commits):
```bash
cp hooks/pre-commit .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

The CI workflow in [.github/workflows/ci.yml](.github/workflows/ci.yml) automatically runs tests and code quality checks on every push.

## Versioning

Version is derived from git tags using `hatch-vcs` with `local_scheme = "no-local-version"`:
- Clean tagged commit: `1.0.0`
- Commits after tag: `1.0.1.devN` (where N is commit count after tag)
- No tag exists: `0.1.devN`

Create a tag:
```bash
git tag v1.0.0
```

## Publishing

This project includes a GitHub Actions workflow for publishing to PyPI. See the [pypa/gh-action-pypi-publish](https://github.com/pypa/gh-action-pypi-publish) documentation for configuration details.

## Acknowledgements

This template uses:
- [Click](https://github.com/pallets/click) - For building CLI interfaces
- [colorlog](https://github.com/bkabrda/colorlog) - For colored logging output
- [mypy](https://github.com/python/mypy) - For static type checking

## License

MIT
