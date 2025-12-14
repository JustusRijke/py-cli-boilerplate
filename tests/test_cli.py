from pathlib import Path

from click.testing import CliRunner

from myprogram.cli import cli


def test_cli_runs_without_error():
    runner = CliRunner()
    result = runner.invoke(cli)
    assert result.exit_code == 0


def test_foobar_prints_to_stdout():
    runner = CliRunner()
    result = runner.invoke(cli, ["--foobar", "hello world"])
    assert result.exit_code == 0
    assert "hello world" in result.output


def test_save_log_creates_file():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(cli, ["--save-log"])
        assert result.exit_code == 0
        assert Path("log.txt").exists()


def test_verbose_flag():
    runner = CliRunner()
    result = runner.invoke(cli, ["-v"])
    assert result.exit_code == 0
    assert "myprogram started" in result.output
    assert "Debug logging enabled" not in result.output


def test_double_verbose_flag():
    runner = CliRunner()
    result = runner.invoke(cli, ["-vv"])
    assert result.exit_code == 0
    assert "myprogram started" in result.output
    assert "Debug logging enabled" in result.output
