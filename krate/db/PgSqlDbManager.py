from abc import ABCMeta
from DbManager import DbManager
from ..ObjectsFactory import ObjectsFactory

import psycopg2

class PgSqlDbManager(DbManager):
    __metaclass__ = ABCMeta
    connection = None
    connectionParams = {}
    log = ObjectsFactory.getLogger("pgSqlDbManager")
    
    def __init__(self, hostname, port, username, password, database):
        self.connectionParams['hostname'] = hostname
        self.connectionParams['port'] = port
        self.connectionParams['username'] = username
        self.connectionParams['password'] = password
        self.connectionParams['database'] = database
    
    def connect(self, connectionObject=None):
        connectionObject = connectionObject if connectionObject is not None else self.connectionParams
        
        try:
            self.connection = psycopg2.connect(database = connectionObject['database'],
                                   user     = connectionObject['username'],
                                   password = connectionObject['password'],
                                   port     = connectionObject['port'])
        except KeyError:
            self.log.exception("This is a key error, but since it does not depend on user input, this is not really supposed to happen")
            raise AssertionError()
    
    def run_query(self, query):
        if self.connection is not None:
            cursor = self.connection.cursor()
            cursor.execute(query)
            
            return cursor
        else:
            raise AssertionError()
