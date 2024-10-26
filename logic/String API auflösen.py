from Ausgabe_API import Ausgabe_API

class API_auflösen():
    
    API = (Ausgabe_API.Funktion_API_einlesen().split("[")[1])   # entfernt die Kopfzeile, trennt den restlichen String
    API = API.split("}, ")
    x = len(API)
    i = 0
    Daten = []
    while i < (x-1):
        Datensatz = (API[i].split("'date': '"))[1]
        Daten.append(Datensatz)
        i = i+1
    letzter_Datensatz = (API[x-1].split("},"))[0]
    letzter_Datensatz = letzter_Datensatz.split("'date': '")[1]    
    Daten.append(letzter_Datensatz)
    print (Daten[1])
    x = len(Daten)
    i = 0
    Datum = []
    Rest = []
    while i < x:
        Datum_1 = Daten[i]
        Datum_2 = Datum_1.split("T")
        #Rest_1 = (Daten[i].split("; "))[1]
        Datum.append(Datum_2)
        #Rest.append(Rest)
        i = i+1
    print (Datum[1])
    #print (Rest[1])
    
                          