import csv
from typing import Optional
from Datentypen.stromanbieter import Stromanbieter
from logic.logicApi import LogicApi

urlBoersenApi:str = 'https://apis.smartenergy.at/market/v1/price'
logic_api_instance = LogicApi(urlBoersenApi)

anbieter1:Optional[Stromanbieter] = logic_api_instance.erstelleStromanbieter("Anbieter A")

if anbieter1 is not None:
    print("Anbieter gespeichert in DB:")
    print(anbieter1)
    print(anbieter1.stundenpreise[0].value)
else:
    print("kein Api Zugriff oder Zugriff auf DB moeglich")

anbieter2:Optional[Stromanbieter] = logic_api_instance.erstelleStromanbieter("Anbieter B")
if anbieter2 is not None:
    print(anbieter2)
else:
    print("kein Api Zugriff moeglich")


with open('stromanbieter_preise.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['name', 'date', 'value'])  # Header-Zeile
    for preis in anbieter1.stundenpreise:
        writer.writerow([anbieter1.name, preis.date, preis.value])
    for preis2 in anbieter2.stundenpreise:
        writer.writerow([anbieter2.name, preis2.date, preis2.value])
print("CSV-Datei wurde erstellt.")
#logic_api_instance.fetchAndAddTodayPrices(anbieter1)
# print(anbieter1)


#stundenZeit:int = 12
#logic_api_instance.sammlePreise(anbieter2,stundenZeit)
