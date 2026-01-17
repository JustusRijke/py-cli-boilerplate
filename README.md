# py-cli-boilerplate

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Build](https://github.com/JustusRijke/py-cli-boilerplate/actions/workflows/build.yml/badge.svg)](https://github.com/JustusRijke/py-cli-boilerplate/actions/workflows/build.yml)
[![codecov](https://codecov.io/github/JustusRijke/py-cli-boilerplate/graph/badge.svg?token=PXD6VY28LO)](https://codecov.io/github/JustusRijke/py-cli-boilerplate)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue)](https://www.python.org/downloads/)
![PyPI - Types](https://img.shields.io/pypi/types/py-cli-boilerplate?pypiBaseUrl=https%3A%2F%2Ftest.pypi.org)
[![PyPI - Version](https://img.shields.io/pypi/v/py-cli-boilerplate?pypiBaseUrl=https%3A%2F%2Ftest.pypi.org)](https://test.pypi.org/project/py-cli-boilerplate/)
[![GitHub Release Date](https://img.shields.io/github/release-date/JustusRijke/py-cli-boilerplate)](https://github.com/JustusRijke/py-cli-boilerplate/releases)

An opinionated Python CLI boilerplate template for GitHub-hosted projects.

## Usage as Template

1. [Create a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template#creating-a-repository-from-a-template) directly using this template
1. Replace `py-cli-boilerplate` with your distribution name in all files
1. Replace `py_cli_boilerplate` with your package name in all files (dashes not allowed in package names)
1. Rename `src/py_cli_boilerplate/` directory to your package name
1. Update [pyproject.toml](pyproject.toml) with your project details
1. Update badge URLs in `README.md` with your repository URL

### Optional Setup

- **Enable Dependabot**: Go to Settings > Code security and analysis > Dependabot to enable automatic dependency updates
- **Enable Codecov**: Set up [Codecov](https://codecov.io) integration for code coverage tracking
- **Publishing on PyPI**: See [Publishing](#publishing)
- **Typed Project**: This template is configured as a typed project with the `py.typed` marker and `Typing :: Typed` classifier in [pyproject.toml](pyproject.toml). If your project won't provide type hints, remove `src/py_cli_boilerplate/py.typed` and the typing classifier from pyproject.toml

## Installation (End Users)

### Using uv (preferred method)

[uv](https://github.com/astral-sh/uv?tab=readme-ov-file#installation) automatically handles Python installation and setup in the background so you don't have to.

If your package is available on PyPI, the user can simply run the program using uvx:

```bash
uvx py-cli-boilerplate
```

### Using pip

Make sure [Python](https://www.python.org/downloads/) v3.10 or higher is installed.

Create a virtual environment (optional):

```bash
python -m venv .venv
source .venv/bin/activate
```

Install the package:

```bash
pip install py-cli-boilerplate
```

Or, if the package is not (yet) available on PyPI, clone the repo and:

```bash
pip install .
```

## CLI Usage

```bash
$py-cli-boilerplate --help

Usage: py-cli-boilerplate [OPTIONS] FOOBAR

  FOOBAR is an example argument, its value is printed to stdout

Options:
  -v, --verbose  Increase verbosity (-v for INFO, -vv for DEBUG)
  --save-log     Write log output to log.txt
  --version      Show the version and exit.
  --help         Show this message and exit.
```

Example:

```bash
$py-cli-boilerplate "hello world" -vv

2025-12-15 14:14:32 DEBUG    cli.py:22 (cli): Debug logging enabled
2025-12-15 14:14:32 INFO     cli.py:25 (cli): Program started
hello world
2025-12-15 14:14:32 INFO     cli.py:34 (cli): Program finished
```

## Library Usage

Run from Python:

```python
from py_cli_boilerplate import invoke
invoke(["-vv", "hello world"])
```

## Development

### Installation

Install [uv](https://github.com/astral-sh/uv?tab=readme-ov-file#installation). Then, install dependencies & activate the automatically generated virtual environment:

```bash
uv sync --locked
source .venv/bin/activate
```

Skip `--locked` to use the newest dependencies (this might modify `uv.lock`)

### Testing

Run tests:

```bash
pytest
```

### Quality Assurance (QA)

Automatically run code quality checks before every commit using [pre-commit](https://pre-commit.com/):

```bash
pre-commit install
```

This installs git hooks that run ruff, type checks, and other checks before each commit. You can run manually at any time with:

```bash
pre-commit run --all-files
```

The CI build workflow ([.github/workflows/build.yml](.github/workflows/build.yml)) automatically runs tests and code quality checks on every push.

### Versioning

Version is derived from git tags using `hatch-vcs` with `local_scheme = "no-local-version"`:

- Clean tagged commit: `1.0.0`
- Commits after tag: `1.0.1.devN` (where N is commit count after tag)
- No tag exists: `0.1.devN`

Create a tag via a GitHub release (see [Publishing](#publishing)) or manually using `git tag`.

### Publishing

This project includes a GitHub Actions workflow ([pypi-publish.yml](.github/workflows/pypi-publish.yml)) that uses [pypa/gh-action-pypi-publish](https://github.com/pypa/gh-action-pypi-publish) for publishing to [test.pypi.org](https://test.pypi.org/) (the Test Python Package Index).

To publish:

1. Create an account on [test.pypi.org](https://test.pypi.org/).
1. Add the project to the list of [trusted publishers](https://test.pypi.org/manage/account/publishing/).
1. [Create a release](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository#creating-a-release) on GitHub. This triggers the workflow.

To publish on [pypi.org](https://pypi.org/) instead of test.pypi.org, remove the `repository-url` line from [pypi-publish.yml](.github/workflows/pypi-publish.yml) and remove `pypiBaseUrl` from the PyPI badge url in `README.md`.

## Acknowledgements

This template uses:

- [Click](https://github.com/pallets/click) - For building CLI interfaces

## License

MIT
