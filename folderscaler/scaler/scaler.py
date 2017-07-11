from pathlib import Path

from sys import exc_info
try:
    from os import walk, path
except ImportError:
    from scandir import scandir, walk
import csv
from operator import itemgetter
from collections import OrderedDict


class Scaler:

    def __init__(self, path):
        self.path = path



    def scale(self):
        start_path = self.path
        results = {}
        total_size = 0

        try:
            for root, dirs, files in walk(start_path):
                try:
                    for file in files:

                        full_file_path = path.join(root, file)

                        file_size = path.getsize(full_file_path)

                        results[full_file_path] = file_size
                except:
                    print("Unexpected error:", exc_info()[1])
                    raise

            results_ordered = OrderedDict(sorted(results.items(), key=itemgetter(1), reverse=True))

            return results_ordered

        except FileNotFoundError:
            print("ERROR: Path '{}' cannot be found on the system. Check for typos and try again.".format(start_path))

        except PermissionError:
            print("ERROR: Permission denied for path '{}'."
                  " Run this program with higher permissions and try again.".format(start_path))
        except:
            print("Unexpected error:", exc_info()[1])
            raise






