#from Datentypen.apiData import BoersenpreisApiDaten

#from persistence.persistenceApi import PersistenceApi


from typing import List
import psycopg2
from Datentypen.stromanbieter import Stromanbieter

class DbApi:

    def __init__(self: 'DbApi', host:str, port:str, databaseName:str, user:str, password:str ):
        self.host = host,
        self.port = port
        self.databaseName = databaseName
        self.user = user
        self.password = password

    def ladeStromanbieter(self: 'DbApi')->List[Stromanbieter]:
        try:
            connection = psycopg2.connect(
                host=self.host,
                database=self.databaseName,
                user=self.user,
                password=self.password
            )
            print("Verbindung zur PostgreSQL-Datenbank erfolgreich!")

            # Cursor erstellen, um SQL-Befehle auszuführen
            cursor = connection.cursor()

            # Beispiel-SQL-Abfrage
            cursor.execute("SELECT * FROM meine_tabelle;")

             # Ergebnisse abrufen
            rows = cursor.fetchall()
            for row in rows:
                print(row)

        except (Exception, psycopg2.Error) as error:
            print("Fehler beim Verbinden mit der PostgreSQL-Datenbank:", error)

        finally:
        # Verbindung schließen
            if connection:
                cursor.close()
                connection.close()
                print("Die Verbindung zur Datenbank wurde geschlossen.")