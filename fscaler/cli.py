from time import sleep

import click
from  os import getenv
from os.path import expanduser
from fscaler.scaler.scaler import Scaler
from fscaler.utils import util

home = getenv('HOME')


@click.group()
@click.version_option()
def cli():
    """
        ╬═╬ ███████╗███████╗ ██████╗ █████╗ ██╗     ███████╗██████╗  ╬═╬
        ╬═╬ ██╔════╝██╔════╝██╔════╝██╔══██╗██║     ██╔════╝██╔══██╗ ╬═╬
        ╬═╬ █████╗  ███████╗██║     ███████║██║     █████╗  ██████╔╝ ╬═╬
        ╬═╬ ██╔══╝  ╚════██║██║     ██╔══██║██║     ██╔══╝  ██╔══██╗ ╬═╬
        ╬═╬ ██║     ███████║╚██████╗██║  ██║███████╗███████╗██║  ██║ ╬═╬
        ╬═╬ ╚═╝     ╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝ ╬═╬

    Fscaler is a small utility which helps you find what's taking the most space in your system.

    Examples:   fscaler run

                fscaler run --path '<Path_to_Folder>' --out '<Path_to_Output_Folder>'

                fscaler run --help

    This tool iterates over your file system and may require some permissions.

    For more help using this tool, Read the README, or open an issue on the Github repository:
    https://github.com/ClovisIRex/Fscaler
    """
@cli.command()
@click.option('--path', '-p', default=home, help="Runs on a specific folder's path (default is user's home directory)")
@click.option('--out', '-o', default='-',
              help="Specifies a folder path for .csv file output (default is to print to stdout)")
def run(path, out):

    if path != home:
        path = str(path)

    click.secho("Scaling the path: '%s'. Please wait..." % click.format_filename(path), bold=True, fg="yellow")
    sleep(1)
    scaler = Scaler(path)

    results = scaler.scale()
    sleep(1)

    if bool(results):
        click.secho("Scaling Done !", bold=True, fg="green")
        sleep(1)
    else:
        click.secho("No results! Exiting...", bold=True, fg="red")
        exit()


    if out != '-':
        util.convert_results(results, out, isCsv=True)
    else:
        util.convert_results(results)

if __name__ == '__main__':
    cli()
