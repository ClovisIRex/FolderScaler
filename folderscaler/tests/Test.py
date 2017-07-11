from folderscaler.scaler.scaler import Scaler
from folderscaler.utils import util
from os import getcwd

def test():
    s = Scaler(r'/home/tal/Documents/')
    results = s.scale()

    for i in results.items():
        print(i)




if __name__ == '__main__':
    test()