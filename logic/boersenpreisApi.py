# importiert den aktuellen Preis aus der API
from datetime import datetime
from typing import Optional
import requests

from Datentypen.apiData import BoersenpreisApiDaten
from Datentypen.preis import Preis

class BoersenpreisApi():
    
    def httpAnfrage(url:str)-> Optional[BoersenpreisApiDaten]:
        response: requests.Response = requests.get(url)   
        if response.status_code == 200:
            json_data = response.json()
            pricesConverted = [Preis(datetime.fromisoformat(item['date']), item['value']) for item in json_data['data']]
            data: BoersenpreisApiDaten  = BoersenpreisApiDaten(             
            tariff=json_data.get('tariff'),             
            prices=pricesConverted,             
            unit=json_data.get('unit'),    
            interval=json_data.get('interval') 
            )
            #ignoriere zeitzoneninformationen, damit Datum als Tmiestamp in DB gespeicjert werden kann
            for entry in data.prices:
                entry.date = entry.date.replace(tzinfo=None)
            return data
        else:
            return None
