from typing import List
from dataclasses import dataclass

from Datentypen.preis import Preis

@dataclass
class BoersenpreisApiDaten:
    tariff: str
    unit: str
    interval: int
    data: List[Preis]