import click
from src._1_weather import *
from src._3_forecast import *

@click.group()
def cli():
    pass

#1
cli.add_command(weather)

#3
cli.add_command(forecast)

if __name__ == "__main__":
    cli()

