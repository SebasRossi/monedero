"""This module provides the CLI for Monedero"""
# monedero/cli.py


import click
from datetime import date
from monedero import __app_name__, __version__
from monedero.functions import environment


@click.group(invoke_without_command=True)
@click.option("--version", "-v", is_flag=True, help="Show the version.")
@click.option("--author", "-s", is_flag=True, show_default=True, default=False, help="Show the creator.")
def app(version, author):
    if version:
        click.echo(f"{__app_name__} v{__version__}")
    if author:
        click.echo("El Sebi")

@click.command()
@click.argument("folder")
def bucket(folder):
    # TODO: 
    click.echo(environment(saving_path=folder))

@click.command(help="Get the coins.")
@click.option('--coin', '-c', required=True, help='Get the a specific coin.')
@click.option('--date', '-d', default=date.today(), show_default=False, help="Choose the date to download data  (ISO8601 format, e: 2017-12-30). Today as default.")
def get(coin, date):
    #click.echo(coin)
    click.echo(coin + ' ' + date)

app.add_command(get)
app.add_command(bucket)
