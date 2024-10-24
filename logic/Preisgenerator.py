import random
from Boersenpreis import Boersenpreis

def Funktion_Strompreise():
    StrompreisA = round (random.normalvariate(Boersenpreis.Funktion_Preis(), 0.2), 2)

    StrompreisB = round (random.normalvariate(Boersenpreis.Funktion_Preis(), 0.2), 2)
  
    return StrompreisA
    return StrompreisB 

