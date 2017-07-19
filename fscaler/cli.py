


import click
from fscaler.scaler import scaler
from os.path import expanduser


home = expanduser("~")


@click.command()
@click.option('-h','--help', is_flag=True)
@click.option('-p','--path', default=home)
@click.option('-o','--out', type=click.File('w'), default='-')
@click.version_option()
def cli(help, path, out):


if __name__ == '__main__':
    cli()
