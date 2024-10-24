# importiert den aktuellen Preis aus der API
from typing import Optional
import requests

from Datentypen.apiData import BoersenpreisApiDaten

class BoersenpreisApi():
    
    def httpAnfrage(url:str)-> Optional[requests.Response]:
        response: requests.Response = requests.get(url)   
        if response.status_code == 200:
            data: BoersenpreisApiDaten  = response.json()
            return data
        else:
            return None