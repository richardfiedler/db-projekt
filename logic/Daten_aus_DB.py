import sqlite3

Verbindung = sqlite3.connect("Datenbank.db")                                   # Name der DB fehlt noch
Zeiger = Verbindung.cursor()


zeiger.execute("SELECT ... FROM Datenbank")
inhalt = zeiger.fetchall()
print(inhalt)
verbindung.close()