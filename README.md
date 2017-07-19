    
# Fscaler
    ╬═╬ ███████╗███████╗ ██████╗ █████╗ ██╗     ███████╗██████╗  ╬═╬
    ╬═╬ ██╔════╝██╔════╝██╔════╝██╔══██╗██║     ██╔════╝██╔══██╗ ╬═╬
    ╬═╬ █████╗  ███████╗██║     ███████║██║     █████╗  ██████╔╝ ╬═╬
    ╬═╬ ██╔══╝  ╚════██║██║     ██╔══██║██║     ██╔══╝  ██╔══██╗ ╬═╬
    ╬═╬ ██║     ███████║╚██████╗██║  ██║███████╗███████╗██║  ██║ ╬═╬
    ╬═╬ ╚═╝     ╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝ ╬═╬

    "...And he dreamed, and behold a ladder set up on the earth,
    and the top of it reached to heaven:
    and behold the angels of God ascending and descending on it."

                                                            ~Genesis 28:10-12
                                                                                                              
                                                                                                              
Fscaler is a small utility which helps you find what's taking the most space in your system.
    
## Why not just use du or some GUI tool? 
Mainly because I wanted to make something neat of my own which also works on Windows and exports a csv file.

## Installation
First make sure you have Python and pip installed properly on your system.

Download the repository(either use git,download directly or curl) and inside the directory:
```sh
$ pip install .
```
## Usage
        Usage: fscaler
               fscaler <options> [...]
               fscaler --help
               fscaler --version
        
        Options:
        
          -p --path                         Runs on a specific folder's path (default is user's home directory)
        
          -o --out                          Specifies a folder path for .csv file output (default is to print to stdout)
        
          -h --help                         Show help
        
          --version                         Show version
        
        Examples:
          fscaler --path "<Path_to_Folder>" --out "<Path_to_Output_Folder>"
        
        
        Help:
          This tool runs over your file system and may require some permissions.
          For help using this tool, please open an issue on the Github repository:
          https://github.com/ClovisIRex/Fscaler