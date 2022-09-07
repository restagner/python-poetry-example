from click.testing import CliRunner

from pythonpoetryexample import __version__
from pythonpoetryexample import console
import click.testing


def test_version():
    assert __version__ == "0.1.0"


def test_main_succeeds():
    runner: CliRunner = click.testing.CliRunner()
    result = runner.invoke(console.hello)
    assert result.exit_code == 0
