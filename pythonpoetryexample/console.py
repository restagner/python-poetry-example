import click
from pythonpoetryexample import __version__
from pythonpoetryexample.pages.apollo.apollo_login import ApolloLogin


@click.command()
@click.version_option(version=__version__)
def hello():
    """The python poetry example Python project"""
    click.echo("Hello from a Python project using Poetry")
    apollo_login: ApolloLogin = ApolloLogin('Why, hello there!')
    apollo_login.display_login_page()
