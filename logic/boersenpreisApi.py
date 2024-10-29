# importiert den aktuellen Preis aus der API
from typing import Optional
import requests

from Datentypen.apiData import BoersenpreisApiDaten

class BoersenpreisApi():
    
    def httpAnfrage(url:str)-> Optional[BoersenpreisApiDaten]:
        response: requests.Response = requests.get(url)   
        if response.status_code == 200:
            json_data = response.json()
            data: BoersenpreisApiDaten  = BoersenpreisApiDaten(             
            tariff=json_data.get('tariff'),             
            data=json_data.get('data'),             
            unit=json_data.get('unit'),    
            interval=json_data.get('interval')       
        )
            return data
        else:
            return None
