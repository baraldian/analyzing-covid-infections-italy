import json
import re


def extract_regioni():
    regioni = ['LOMBARDIA', 'EMILIA - ROMAGNA', 'VENETO', 'MARCHE', 'PIEMONTE', 'TOSCANA', 'CAMPANIA', 'LAZIO',
               'LIGURIA', 'FRIULI VENEZIA GIULIA', 'SICILIA', 'PUGLIA', 'UMBRIA', 'ABRUZZO', 'MOLISE',
               'TRENTINO ALTO ADIGE', 'SARDEGNA', 'BASILICATA', 'VALLE D AOSTA', 'CALABRIA']
    provincieRegioni = {}
    with open("bollettini/20-03.txt", 'r') as f:
        text = f.read()

    x = re.findall("(?P<name>[A-Za-z ]+) (?P<number>[0-9]+)", text)

    i = 0
    provincieRegioni[regioni[i]] = []
    for citta in x:
        if citta[0].lower().find('totale') == -1:
            if citta[0].lower().find('verifica') == -1 and citta[0].lower().find('covid')==-1 and citta[0].lower().find('ripartizione')==-1 \
                    and citta[0].lower().find('aggiornamento') == -1:
                provincieRegioni[regioni[i]].append(citta[0].upper())
        else:
            i += 1
            if (i < len(regioni)):
                provincieRegioni[regioni[i]] = []
            else:
                break

    with open('regioni.txt', 'w') as outfile:
        json.dump(provincieRegioni, outfile)


if __name__ == '__main__':
    extract_regioni()
