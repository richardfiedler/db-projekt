from dataclasses import dataclass
from datetime import datetime

@dataclass
class Preis:
    date: datetime
    value: float