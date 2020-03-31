from datetime import datetime
import json


def convert_to_csv():
    with open('dati.raw', 'r', encoding='utf8') as dataFile:
        rilevazioni = json.load(dataFile)

    lines = []
    lines.append('Regione,Citta')
    dati_regione = rilevazioni[list(rilevazioni.keys())[0]]
    dati_citta = dati_regione[list(dati_regione.keys())[0]]

    giorni = list(dati_citta.keys())
    giorni = [ datetime.strptime(element, '%d-%m') for element in giorni]
    giorni = sorted(giorni)
    giorni = [ element.strftime('%d-%m') for element in giorni ]
    for giorno in giorni:
        lines[0] += ',' + giorno
    lines[0] += '\n'

    for regione, dati_cities in rilevazioni.items():
        for citta, dati_citta in dati_cities.items():
            line = regione
            line += ',' + citta
            for giorno in giorni:
                line += ',' + str(dati_citta[giorno])
            lines.append(line + '\n')

    out = open('rilevazioni.csv','w')
    out.writelines(lines)

    out.close()



if __name__ == '__main__':
    convert_to_csv()