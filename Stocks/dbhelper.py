import pymysql


class DbHelper(object):
    CREATE_DB = "CREATE DATABASE PythonDataBase "
    CREATE_SHARES = "CREATE TABLE PythonDataBase.Shares ( share_code VARCHAR(45) NOT NULL," \
                    "share_name VARCHAR(45) NOT NULL," \
                    "high FLOAT NOT NULL," \
                    "low FLOAT NOT NULL," \
                    "volume INT NOT NULL," \
                    "trade FLOAT NOT NULL," \
                    "PRIMARY KEY (share_code))"
    CREATE_PERSONS = "CREATE TABLE PythonDataBase.Persons ( id INT NOT NULL AUTO_INCREMENT," \
                     "first_name VARCHAR(45) NOT NULL," \
                     "last_name VARCHAR(45) NOT NULL," \
                     "PRIMARY KEY (id))"

    def __init__(self, host, user, port):
        self.conn = pymysql.connect(host=host, user=user, port=port, passwd="root", charset="utf8")
        self.cursor = self.conn.cursor()
        self.cursor.execute("DROP DATABASE IF EXISTS PythonDataBase")
        self.cursor.execute(self.CREATE_DB)
        self.cursor.execute("DROP TABLE IF EXISTS PythonDataBase.Shares")
        self.cursor.execute("DROP TABLE IF EXISTS PythonDataBase.Persons")
        self.cursor.execute(self.CREATE_SHARES)
        self.cursor.execute(self.CREATE_PERSONS)

    def close(self):
        self.cursor.close()