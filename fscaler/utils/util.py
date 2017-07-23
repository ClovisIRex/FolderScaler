import csv
import math
from os import getcwd
from sys import exc_info
from click import echo_via_pager, progressbar, secho, format_filename, echo
from tabulate import tabulate




def convert_bytes(size):
    """
    This method will convert bytes to MB & GB
    """
    if (size == 0):
        return '0 Bytes'

    size_name = ("Bytes", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")

    i = int(math.floor(math.log(size, 1024)))
    p = math.pow(1024, i)
    s = round(size / p, 2)

    return '%s %s' % (s, size_name[i])


def convert_results(sizedict, csvpath=getcwd(), isCsv = False):
    """
           convert_to_csv(dict, pathlib.posixPath) -> None

           This method gets a dictionary of file paths and their sizes,
           formats them in MB and GB, and converts it into a csv file
           which is saved into the current directory by default

           :param sizedict: a dictionary of file paths and their sizes.

           :param csvpath: a posixpath object describing where to output the csv file

           :return None
    """
    newdict = {}

    for item in sizedict.items():
        newdict['%-12s' % format_filename(item[0])] = '%-12s' % convert_bytes(item[1])

    try:
        if isCsv:
            with progressbar(length=len(newdict), label="Converting to csv...") as progress:
                with open(r'{}/fscaler.csv'.format(csvpath), 'w', newline='') as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(["Path", "Size"])

                    for filepath, size in newdict.items():
                        writer.writerow([filepath, size])
                        progress.update(1)
            secho("csv output was saved in path: {}".format(csvpath), bold=True, fg="green")
        else:
            secho("Preapring output...",bold=True, fg="yellow")

            echo_via_pager(tabulate(newdict.items()))



    except PermissionError:
        secho("ERROR: Write permission denied for path '{}'."
              " Run this program with higher permissions and try again.".format(csvpath),fg='red', bold=True )
        exit()
    except:
        secho("Unexpected error: {}".format(exc_info()[1]),fg='red', bold=True)
        exit()
