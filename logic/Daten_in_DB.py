import sqlite3

Verbindung = sqlite3.connect("Datenbank.db")                                   # Name der DB fehlt noch
Zeiger = Verbindung.cursor()


Wochentag = ""
Datum = ""
Uhrzeit = ""
Preis = ""

Zeiger.execute("""
                INSERT INTO Datenbank 
                       VALUES (?,?,?,?)
               """, 
              (Wochentag, Datum, Uhrzeit, Preis)
              )

Verbindung.commit()
Verbindung.close()