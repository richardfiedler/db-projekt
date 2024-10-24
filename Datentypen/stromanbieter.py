from dataclasses import dataclass
from typing import List
from Datentypen.preis import Preis

@dataclass
class Stromanbieter:
    name: str
    stundenpreise: List[Preis]