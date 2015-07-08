import pymysql
from config import config

class dbc():

    def __init__(self, dbHost='localhost', dbName='teach_me', username=config['dbUser'], password=config['dbPassword']):
        self._conn = pymysql.connect(host=dbHost, port=3306, user=username, passwd=password, db=dbName)
        self._cursor = self._conn.cursor()


    def resultTuple(self, query):
        self._cursor.execute(query)
        return self._cursor.fetchall()


    def resultDict(self, query):
        self._cursor = self._conn.cursor(pymysql.cursors.DictCursor)
        self._cursor.execute(query)
        return self._cursor.fetchall


    def resultSingle(self, query):
        self._cursor.execute(query)
        return self._cursor.fetchone()

    def execute(self, query):
        self._cursor.execute(query)
        self._conn.commit()


    def __del__(self):
        self._conn.close()