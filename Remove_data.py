import argparse
from datetime import datetime
import json
from Convert_to_csv import  convert_to_csv


def load_regioni():
    with open('regioni.txt') as json_file:
        data = json.load(json_file)
    return data

def remove(data):

    provincieRegioni = load_regioni()

    with open('dati.raw', 'r', encoding='utf8') as dataFile:
        dati = json.load(dataFile)
    for regione, dati_cities in dati.items():
        for citta, dati_citta in dati_cities.items():
            del dati_citta[data]

    with open('dati.raw','w') as outfile:
        json.dump(dati, outfile, ensure_ascii=False)

    return 0



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("data", help="Giorno rilevazione", type=lambda s: datetime.strptime(s, '%d-%m'))
    args = parser.parse_args()
    data = datetime.strftime(args.data,"%d-%m")
    remove(data)
    convert_to_csv()
