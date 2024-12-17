
from Datentypen.stromanbieter import Stromanbieter
from persistence.dbApi import DbApi
from persistence.fileapi import FileApi


class PersistenceApi:


    def __init__(self: 'PersistenceApi', host:str, port: str, databaseName:str, user:str, password:str, csvFile:str):
        self.dbApi = DbApi(host=host, port = port, databaseName = databaseName, user=user, password=password)
        self.csvFileName = csvFile

    def writeCsv(self: 'PersistenceApi', anbieter:Stromanbieter):
        FileApi.writeCsv(self.csvFileName,anbieter)

    def ladeStromanbieter(self: 'PersistenceApi'):
        self.dbApi.ladeStromanbieter()