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
    x = len(Daten)
    i = 0
    Daten_1 = []
    while i < x:                                                # trennt den String auf zur Weiterverarbeitung
        String_Daten = Daten[i]
        Liste_Daten = String_Daten.split("T")
        Daten_1.append(Liste_Daten)                             # "T" verschwindet aus String, Datum und Uhrzeit sind getrennte Werte
        Wert_Datum = Daten_1[i]
        Tag = (Wert_Datum[0].split("-"))[2] 
        Monat = (Wert_Datum[0].split("-"))[1]
        Jahr = (Wert_Datum[0].split("-"))[0]                    # String in Tag, Monat, Jahr aufgetrennt
        Wert_Rest = Daten_1[i]
        Uhrzeit = (Wert_Rest[1].split("+"))[0]                  # Uhrzeit ohne + 2:00 Angabe
        Wert_Preis= (Wert_Rest[1].split("', 'value': "))[1]     # Preis in Cent
        # Hier erfolgt die Übergabe der ermittelten Werte in die Tabelle
        i = i+1
    
                          
