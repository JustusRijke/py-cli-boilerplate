from pathlib import Path

from click.testing import CliRunner

from pycliboilerplate.cli import cli


def test_cli_runs_without_error():
    runner = CliRunner()
    result = runner.invoke(cli, ["hello world"])
    assert result.exit_code == 0


def test_save_log_creates_file():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(cli, ["hello world", "--save-log"])
        assert result.exit_code == 0
        assert Path("log.txt").exists()


def test_verbose_flag():
    runner = CliRunner()
    result = runner.invoke(cli, ["hello world", "-v"])
    assert result.exit_code == 0
    assert "pycliboilerplate started" in result.output
    assert "Debug logging enabled" not in result.output


def test_double_verbose_flag():
    runner = CliRunner()
    result = runner.invoke(cli, ["hello world", "-vv"])
    assert result.exit_code == 0
    assert "pycliboilerplate started" in result.output
    assert "Debug logging enabled" in result.output
