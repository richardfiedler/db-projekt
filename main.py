from typing import Optional
from Datentypen.stromanbieter import Stromanbieter
from logic.logicApi import LogicApi

urlBoersenApi:str = 'https://apis.smartenergy.at/market/v1/price'
logic_api_instance = LogicApi(urlBoersenApi)

anbieter1:Optional[Stromanbieter] = logic_api_instance.erstelleStromanbieter("Anbieter A")

if anbieter1 is not None:
    print(anbieter1)
else:
    print("kein Api Zugriff moeglich")

anbieter2:Optional[Stromanbieter] = logic_api_instance.erstelleStromanbieter("Anbieter B")
if anbieter2 is not None:
    print(anbieter2)
else:
    print("kein Api Zugriff moeglich")


logic_api_instance.fetchAndUpdate(anbieter1)
print(anbieter1)

stundenZeit:int = 12
logic_api_instance.aktualisierePreisliste(anbieter2,stundenZeit)
