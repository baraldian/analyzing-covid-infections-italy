import re
import argparse

from datetime import datetime
import json


def load_regioni():
    with open('regioni.txt') as json_file:
        data = json.load(json_file)
    return data

def extract(text_file, data):

    provincieRegioni = load_regioni()
    with open(text_file,'r', encoding="utf8") as f:
        text = f.read()

    x = re.findall("(?P<name>[A-Za-z ]+) (?P<number>[0-9.]+)", text)
    rilevazioni = { citta.upper() : int(numero.replace('.','')) for citta, numero in x }

    try:
        with open('dati.raw', 'r', encoding='utf8') as dataFile:
            dati = json.load(dataFile)
        for regione, dati_cities in dati.items():
            for citta, dati_citta in dati_cities.items():
                dati_citta[data] = ( rilevazioni[citta] if citta in rilevazioni.keys() else 0)
    except Exception as e:
        dati = { regione : { citta : { data : (rilevazioni[citta] if citta in rilevazioni.keys() else 0) } for citta in cities} for regione, cities in provincieRegioni.items() }


    with open('dati.raw','w') as outfile:
        json.dump(dati, outfile, ensure_ascii=False)



    return 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("text_file",  type=str)
    parser.add_argument("data", help="Giorno rilevazione", type=lambda s: datetime.strptime(s, '%d-%m'))
    args = parser.parse_args()
    data = datetime.strftime(args.data,"%d-%m")
    extract(args.text_file, data)


