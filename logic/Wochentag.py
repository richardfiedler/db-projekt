import datetime
# import der Funktion zur Ermittlung des Datums

class Wochentag():
    
    def Funktion_Wochentag_ermitteln():
        
       #Datum im Format Jahr-Monat-Tag übergeben
     
       Datum = 
       Datum = datetime.datetime.strptime(Datum,'%Y-%m-%d').date()             # Umwandlung String in Datumsformat
       Wochentag = Datum.weekday()                                             # Ermittlung WOchentag (Montag = 0, ...)
        
       return Wochentag