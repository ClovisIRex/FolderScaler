from sys import exc_info
from operator import itemgetter
from collections import OrderedDict
from os import path
from pathlib import Path
from click import echo, progressbar, format_filename, secho

try:
    from os import walk
except ImportError:
    from scandir import scandir, walk



class Scaler:
    """
        A class for scaling files and directories in a given path.

        :param path: (string)  describing a path on the file system to scale.
    """

    def __init__(self, path):
        self.path = path

    def scale(self):

        """
               scale(self) -> OrderedDict

               This method performs a walk over the class instance's path,
               and returns all the files in that path sorted by their size in a dictionary.

               :return OrderedDict
        """
        try:
            start_path = self.path

        except FileNotFoundError:
            secho("ERROR: Path '{}' cannot be found on the system. Check for typos and try again.".format(start_path), fg='red', bold=True)
            exit()

        results = {}
        total_size = 0

        try:
            for root, dirs, files in walk(start_path):
                for file in files:

                    full_file_path = path.join(root, file)

                    try:
                        file_size = path.getsize(full_file_path)

                    except FileNotFoundError:
                        continue

                    results[full_file_path] = file_size


            results_ordered = OrderedDict(sorted(results.items(), key=itemgetter(1), reverse=True))

            return results_ordered

        except PermissionError:
            secho("ERROR: Permission denied for path '{}'."
                  " Run this program with higher permissions and try again.".format(start_path), fg='red', bold=True)
            exit()
        except:
            secho("Unexpected error:", exc_info()[1], fg='red', bold=True)
            exit()






