
import random


import time
from sched import scheduler
from datetime import datetime, timedelta

import requests
from logic.boersenpreisApi import BoersenpreisApi
from Datentypen.apiData import BoersenpreisApiDaten
from typing import List, Optional
from Datentypen.stromanbieter import Stromanbieter
from Datentypen.preis import Preis


class LogicApi:


    def __init__(self: 'LogicApi', urlBoersenApi:str):
        self.url = urlBoersenApi

    #zu bestehender Preisliste wird einmal taeglich zu eienr stunde die Liste von Tagespreisen hinzgefuegt
    #sideeffect auf preisliste des stromanbieter
    def aktualisierePreisliste(self: 'LogicApi', anbieter:Stromanbieter, stundenZeit):
        s = scheduler(time.time, time.sleep)
        self._planen(anbieter, s, stundenZeit)
        while True:
            s.run()
            self._planen(anbieter, s, stundenZeit)

    def erstelleStromanbieter(self: 'LogicApi', name:str) -> Optional[Stromanbieter] :
        response:Optional[requests.Response] = BoersenpreisApi.httpAnfrage(self.url)
        if response is not None:
            preisListe:List[Preis] = self._erstellePreisliste(response)
            stromanbieter = Stromanbieter(name=name, stundenpreise=preisListe)
            return stromanbieter
        else:
            return None
        
    def _filterNachStundenpreis(self: 'LogicApi', prices:List[Preis]):
        stundenpreise:List[Preis] = []
        for entry in prices:
            date_str:str = entry['date']
            dt:datetime = datetime.fromisoformat(date_str[:-6])  
            if dt.minute == 0 and dt.second == 0:
                stundenpreise.append(entry)
        return stundenpreise

    def _randomisiere( self: 'LogicApi', preisListe:List[Preis]) ->  List[Preis]:
        for entry in preisListe:
            alterWert = entry['value']
            neuerWert = round(random.normalvariate(alterWert, 0.2), 2)
            entry['value'] = neuerWert
        return preisListe
    
    def _erstellePreisliste(self: 'LogicApi', response:requests.Response) -> List[Preis]:
        apiDaten:BoersenpreisApiDaten = response
        preisListeBoerseViertelstuendlich:List[Preis] = apiDaten['data']
        preisListeBoerseStuendlich:List[Preis] = self._filterNachStundenpreis(preisListeBoerseViertelstuendlich)
        preisListeRandomisiert = self._randomisiere(preisListeBoerseStuendlich)
        return preisListeRandomisiert
    
    def fetchAndUpdate(self: 'LogicApi', anbieter:Stromanbieter):
        response:Optional[requests.Response] = BoersenpreisApi.httpAnfrage(self.url)
        if response is not None:
            preisListe:List[Preis] = self._erstellePreisliste(response)
            #TODO Richard: nur append, wenn Datum nicht schon enthalten
            anbieter.stundenpreise.append(preisListe)
        else:
            return None
        
    def _planen(self: 'LogicApi', anbieter:Stromanbieter, s:scheduler, stundenZeit:int):
        now = datetime.now()
        next_run = now.replace(hour=stundenZeit, minute=0, second=0, microsecond=0)
        # Wenn die Zeit schon nach 12 Uhr ist, plane den nächsten Tag
        if now >= next_run:
            next_run += timedelta(days=1)
        # Berechne die Zeit bis zur nächsten Ausführung
        wait_time = (next_run - now).total_seconds()
        # Plane die Funktion
        s.enter(wait_time, 1, self.fetchAndUpdate(anbieter))
   