"""
FolderScaler - A small utility which helps you find what's taking the most space in your system.

Usage: folderscaler root
       folderscaler <options> [...]
       folderscaler -h | --help
       folderscaler -version

Options:

  -p --path                         Runs on a specific folder's path.

  -o --out                          Specifies a folder path for .csv file output.

  -f --files                        Include files as well as folders (default is folders only).

  -h --help                         Show this screen.

  --version                         Show version.

Examples:
  folderscaler --path "<Path_to_Folder>" --out "<Path_to_Output_Folder>" --files


Help:
  This tool runs over your file system and may require some permissions.
  For help using this tool, please open an issue on the Github repository:
  https://github.com/ClovisIRex/FolderScaler
"""


import click
from folderscaler.scaler import scaler



@click.command()
@click.option('-p', help="Runs on a specific folder's path(Default is user's home directory).")
#@click.option('-o', is_flag=True, help="Specifies a folder path for .csv file output.")
#@click.option('-f', is_flag=True, help="Include files as well as folders (default is folders only).")
def main():
  print("hello")
    


if __name__ == '__main__':
    main()
