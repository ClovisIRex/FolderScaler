from folderscaler.scaler.scaler import Scaler
from folderscaler.utils import util
from os import getcwd

def test():
    s = Scaler(r'/home/tal/Documents/')
    results = s.scale()

    util.convert_results_to_csv(results)




if __name__ == '__main__':
    test()