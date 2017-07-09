
class util:

    @staticmethod
    def convert_bytes(self, num):
        """
        This method will convert bytes to MB & GB
        """
        for x in ['MB', 'GB']:
            if num < 1024.0:
                return "%3.1f %s" % (num, x)
            num /= 1024.0

    @staticmethod
    def convert_to_csv(self, sizedict, csvpath=Path('.')):
        """
               convert_to_csv(dict, pathlib.posixPath) -> None
    
               This method gets a dictionary of file paths and their sizes in MB and GB, and converts it into a csv file
               which is saved into the current directory by default
    
               @param sizedict: a dictionary of file paths and their sizes in MB and GB.
    
               @param csvpath: a posixpath object describing where to output the csv file
    
               @return None
        """
        with open('{}\\temp.csv'.format(csvpath), 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["Size in MB", "Size in GB", "Path"])
            for path, size in sizedict.items():
                writer.writerow([size, path])

    @staticmethod
    def get_file_size(self, filepath=Path.home()):
        """
        get_file_size(string) -> string
    
        this method will calculate a file size in MB & GB and returns the sizes in a string
    
        @param filepath: a string containing a path to the file
    
        @return string
        """
        file = Path("{}".format(filepath))
        return self.convert_bytes(file.stat().st_size)
