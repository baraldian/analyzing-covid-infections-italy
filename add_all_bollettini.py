from  Extract_to_raw import extract
from datetime import datetime
import argparse
from Convert_to_csv import  convert_to_csv
import os


if __name__ == '__main__':

    bollettini_path = os.path.join(os.path.abspath('.'), 'bollettini')
    f = []
    for (dirpath, dirnames, filenames) in os.walk(bollettini_path):
        f.extend(filenames)
        break
    for bollettino in f:
        data = bollettino[:-4]
        extract('./bollettini/'+data+'.txt', data)
    convert_to_csv()
