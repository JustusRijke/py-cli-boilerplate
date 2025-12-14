# py-cli-boilerplate

[![CI](https://github.com/JustusRijke/py-cli-boilerplate/actions/workflows/ci.yml/badge.svg)](https://github.com/JustusRijke/py-cli-boilerplate/actions/workflows/ci.yml)
[![codecov](https://codecov.io/github/JustusRijke/py-cli-boilerplate/graph/badge.svg?token=PXD6VY28LO)](https://codecov.io/github/JustusRijke/py-cli-boilerplate)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A minimal Python CLI boilerplate template.

## Usage as Template

1. Clone this repository
2. Find and replace `myprogram` with your desired program name
3. Rename `src/myprogram/` directory to match your program name
4. Update [pyproject.toml](pyproject.toml) with your project details

## Installation

Install the package:
```bash
pip install .
```

Install with dev dependencies (pytest, ruff):
```bash
pip install -e .[dev]
```

## CLI Usage

```bash
myprogram [OPTIONS]
```

Options:
- `--foobar TEXT`: Example argument; prints value to stdout
- `--debug`: Set log level to DEBUG (default: INFO)
- `--save-log`: Write log output to `log.txt` in current directory
- `--version`: Show version and exit
- `--help`: Show help and exit

Example:
```bash
myprogram --foobar "hello world" --debug --save-log
```

## Library Usage

Call the CLI from Python:
```python
from myprogram import main
main(["--foobar", "hello world"])
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
```

Install pre-commit hook (runs ruff automatically before commits):
```bash
cp hooks/pre-commit .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

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

## License

MIT
