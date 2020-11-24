import pandas as pd
import pymysql
import mysql.connector
from api.settings import DATABASES as db

class connect ():
    def execQuery(self, query):
        connection = pymysql.connect(host=db['mysql']['host'],
                                     database=db['mysql']['database'],
                                     user=db['mysql']['user'],
                                     password=db['mysql']['password'],
                                     autocommit=True,
                                     local_infile=True)

        try:
            df = pd.read_sql(query, connection)
            result = df.to_dict('records')
            return result
        except mysql.connector.Error as error:
            connection.close()
            return "parameterized query failed: ".format(error)
