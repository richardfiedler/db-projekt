
import random


import time
from sched import scheduler
from datetime import datetime, timedelta

import requests
from logic.boersenpreisApi import BoersenpreisApi
from persistence.fileapi import FileApi
from Datentypen.apiData import BoersenpreisApiDaten
from typing import List, Optional
from Datentypen.stromanbieter import Stromanbieter
from Datentypen.preis import Preis
from persistence.persistenceApi import PersistenceApi


class LogicApi:


    def __init__(self: 'LogicApi', urlBoersenApi:str, persistenceApi:PersistenceApi):
        self.url = urlBoersenApi
        self.persistenceApi = persistenceApi

    #zu bestehender Preisliste wird einmal taeglich zu eienr stunde die Liste von Tagespreisen hinzgefuegt
    #sideeffect auf preisliste des stromanbieter
    def sammlePreise(self: 'LogicApi', anbieter:Stromanbieter, stundenZeit:int):
        s = scheduler(time.time, time.sleep)
        self._planen(anbieter, s, stundenZeit)
        while True:
            s.run()
            self._planen(anbieter, s, stundenZeit)

    def erstelleStromanbieter(self: 'LogicApi', name:str) -> Optional[Stromanbieter] :
        response:Optional[BoersenpreisApiDaten] = BoersenpreisApi.httpAnfrage(self.url)
        if response is not None:
            preisListe:List[Preis] = self._erstellePreisliste(response)
            stromanbieter = Stromanbieter(name=name, stundenpreise=preisListe)
            ##TODO yael -> dbApi.erstelleStromanbieter(stromanbieter)
            ##TODO richard: exception handling falls kein zugriff auf db möglich
            return stromanbieter
        else:
            return None
    #nimm stundenpreis -> date strings mit minute = 00 und sekunde = 00
    def _filterNachStundenpreis(self: 'LogicApi', preise:List[Preis]) -> List[Preis]:
        stundenpreise:List[Preis] = []
        for preis in preise:
            #date_str:str = preis['date']
            #dt:datetime = datetime.fromisoformat(date_str[:-6])  
            dt = preis.date
            if dt.minute == 0 and dt.second == 0:
                stundenpreise.append(preis)
        return stundenpreise

    def _randomisierePreise( self: 'LogicApi', preisListe:List[Preis]) ->  List[Preis]:
        for entry in preisListe:
            alterWert = entry.value#entry['value']
            neuerWert = round(random.normalvariate(alterWert, 0.2), 2)
            #entry['value'] = neuerWert
            entry.value = neuerWert
        return preisListe
    
    def _erstellePreisliste(self: 'LogicApi', apiDaten:BoersenpreisApiDaten) -> List[Preis]:
        #apiDaten:BoersenpreisApiDaten = response
        preisListeBoerseViertelstuendlich:List[Preis] = apiDaten.prices#apiDaten['data']
        preisListeBoerseStuendlich:List[Preis] = self._filterNachStundenpreis(preisListeBoerseViertelstuendlich)
        preisListeRandomisiert = self._randomisierePreise(preisListeBoerseStuendlich)
        return preisListeRandomisiert
    
    def fetchAndAddTodayPrices(self: 'LogicApi', anbieter:Stromanbieter):
        response:Optional[BoersenpreisApiDaten] = BoersenpreisApi.httpAnfrage(self.url)
        if response is not None:
            preisListe:List[Preis] = self._erstellePreisliste(response)
            anbieter.stundenpreise.append(preisListe)
        else:
            return None
        
    def writeCsv(self: 'LogicApi', anbieter:Stromanbieter):
        self.persistenceApi.writeCsv(anbieter)

    def ladeStromanbieter(self: 'LogicApi')->List[Stromanbieter]:
          self.persistenceApi.ladeStromanbieter()

    def _planen(self: 'LogicApi', anbieter:Stromanbieter, s:scheduler, stundenZeit:int):
        now = datetime.now()
        next_run = now.replace(hour=stundenZeit, minute=0, second=0, microsecond=0)
        # Wenn die Zeit schon nach 12 Uhr ist, plane den nächsten Tag
        if now >= next_run:
            next_run += timedelta(days=1)
        # Berechne die Zeit bis zur nächsten Ausführung
        wait_time = (next_run - now).total_seconds()
        # Plane die Funktion
        s.enter(wait_time, 1, self.fetchAndAddTodayPrices(anbieter))
   