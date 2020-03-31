from  Extract_to_raw import extract
from datetime import datetime
import argparse
from Convert_to_csv import  convert_to_csv


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("data", help="Giorno rilevazione", type=lambda s: datetime.strptime(s, '%d-%m'))
    args = parser.parse_args()
    data = datetime.strftime(args.data,"%d-%m")
    extract('./bollettini/'+data+'.txt', data)
    convert_to_csv()
