import os
from pathlib import Path
import csv
from operator import itemgetter
from collections import OrderedDict


class Scaler:

    def __init__(self, path):
        
        self.path = path


    def scale_folders(self):
        start_path = Path(self.path)
        results = ({})
        for root, dirs in os.walk(start_path):
            print('{} : {}'.format(root, dirs))
        return results






