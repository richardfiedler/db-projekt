import csv
from typing import List
from Datentypen.stromanbieter import Stromanbieter


class FileApi():
    def writeCsv(dateiname:str, listeVonStromanbietern:List[Stromanbieter]):
        with open(dateiname, mode='a', newline='') as file:
            writer = csv.writer(file)
            #writer.writerow(['name', 'date', 'value'])  # Header-Zeile
            for anbieter in listeVonStromanbietern:
                for preis in anbieter.stundenpreise:
                    writer.writerow([anbieter.name, preis.value, preis.date])
        print("CSV-Datei wurde geschrieben.")