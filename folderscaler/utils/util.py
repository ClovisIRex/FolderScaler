from os import getcwd
from sys import exc_info
import csv
import math
from pathlib import Path


def convert_bytes(size):
    """
    This method will convert bytes to MB & GB
    """
    if (size == 0):
        return '0B'
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size, 1024)))
    p = math.pow(1024, i)
    s = round(size / p, 2)
    return '%s %s' % (s, size_name[i])


def convert_results_to_csv(sizedict, csvpath=getcwd()):
    """
           convert_to_csv(dict, pathlib.posixPath) -> None

           This method gets a dictionary of file paths and their sizes,
           formats them in MB and GB, and converts it into a csv file
           which is saved into the current directory by default

           @param sizedict: a dictionary of file paths and their sizes.

           @param csvpath: a posixpath object describing where to output the csv file

           @return None
    """
    newdict = {}

    for item in sizedict.items():
        newdict[item[0]] = convert_bytes(item[1])

    try:
        with open(r'{}/folderscaler.csv'.format(csvpath), 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["Path", "Size"])

            for filepath, size in newdict.items():
                writer.writerow([filepath, size])

    except PermissionError:
        print("ERROR: Permission denied for path '{}'."
              " Run this program with higher permissions and try again.".format(csvpath))
    except:
        print("Unexpected error:", exc_info()[1])
        raise
