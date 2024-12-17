import csv
from typing import List, Optional
from Datentypen.stromanbieter import Stromanbieter
from logic.logicApi import LogicApi
from persistence.persistenceApi import PersistenceApi


persistenceApi_instance = PersistenceApi("hsotname","portname","databseName","user","password","stromanbieter_preise.csv")
urlBoersenApi:str = 'https://apis.smartenergy.at/market/v1/price'
logic_api_instance = LogicApi(urlBoersenApi,persistenceApi_instance)

anbieter1:Optional[Stromanbieter] = logic_api_instance.erstelleStromanbieter("Stromanbieter A")

if anbieter1 is None:
    raise Exception("kein Api Zugriff moeglich")

anbieter2:Optional[Stromanbieter] = logic_api_instance.erstelleStromanbieter("Stromanbieter B")

if anbieter2 is None:
    raise Exception("kein Api Zugriff moeglich")

stromanbieter:List[Stromanbieter] = [anbieter1, anbieter2]
logic_api_instance.writeCsv(stromanbieter) 

#geladeneStromanbieter:List[Stromanbieter] = logic_api_instance.ladeStromanbieter(persistenceApi_instance)

#logic_api_instance.fetchAndAddTodayPrices(anbieter1)
# print(anbieter1)

#stundenZeit:int = 12
#logic_api_instance.sammlePreise(anbieter2,stundenZeit)
