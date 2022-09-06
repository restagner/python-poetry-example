import click
from python_poetry_example import __version__


@click.command()
@click.version_option(version=__version__)
def hello():
    """The python poetry example Python project"""
    click.echo("Hello from a Python project using Poetry")
