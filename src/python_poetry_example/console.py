import click
import math
# from python_poetry_example import __version__
#
#
# @click.command()
# @click.version_option(version=__version__)
# def hello():
#     """The python poetry example Python project"""
#     click.echo("Hello from a Python project using Poetry")
#
#
# if __name__ == '__main__':
#     hello()


def area_of_circle(radius: int) -> str:
    pi: float = math.pi
    area: float = pi * (radius ** 2)
    return f'Area = {area:.2f}'


rad: int = 3
print(f'{area_of_circle(rad)}')
