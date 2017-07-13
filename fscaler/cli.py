


import click
from fscaler.scaler import scaler

@click.command()
def main():
    click.echo("""
    ╬═╬ ███████╗███████╗ ██████╗ █████╗ ██╗     ███████╗██████╗  ╬═╬
    ╬═╬ ██╔════╝██╔════╝██╔════╝██╔══██╗██║     ██╔════╝██╔══██╗ ╬═╬
    ╬═╬ █████╗  ███████╗██║     ███████║██║     █████╗  ██████╔╝ ╬═╬
    ╬═╬ ██╔══╝  ╚════██║██║     ██╔══██║██║     ██╔══╝  ██╔══██╗ ╬═╬
    ╬═╬ ██║     ███████║╚██████╗██║  ██║███████╗███████╗██║  ██║ ╬═╬
    ╬═╬ ╚═╝     ╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝ ╬═╬  
                                                                                                              
                                                                                                              
    fscaler - A small utility which helps you find what's taking the most space in your system.
        
        Usage: fscaler
               fscaler <options> [...]
               fscaler --help
               fscaler --version
        
        Options:
        
          -p --path                         Runs on a specific folder's path (default is user's home directory)
        
          -o --out                          Specifies a folder path for .csv file output (default is to print to stdout)
        
          -h --help                         Show this screen
        
          --version                         Show version
        
        Examples:
          fscaler --path "<Path_to_Folder>" --out "<Path_to_Output_Folder>"
        
        
        Help:
          This tool runs over your file system and may require some permissions.
          For help using this tool, please open an issue on the Github repository:
          https://github.com/ClovisIRex/Fscaler
    """)

if __name__ == '__main__':
    main()
