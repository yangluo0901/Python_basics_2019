import pymysql
from dbhelper import DbHelper



class DbManager(object):
    HOST = "localhost"
    PORT = 3306
    USER = "root"
    PASSWD = "root"
    DB = "PythonDataBase"

    def __init__(self):
        self.__db_helper = DbHelper(self.HOST, self.USER, self.PORT)
        self.cursor = self.__db_helper.cursor

    def add_share_entry(self, share):
        sql = "INSERT INTO PythonDataBase.Shares VALUES (%s, %s, %s, %s, %s, %s)"
        self.cursor.execute(sql, (share.code, share.name, share.high, share.low, share.volume, share.trade))
        self.change_commit()

    def add_person_entry(self, person):
        sql = "INSERT INTO PythonDataBase.Persons VALUES (NULL, %s, %s)"
        self.cursor.execute(sql, (person.first_name, person.last_name))
        self.change_commit()

    def update_share_entry(self, share):
        sql = ''' UPDATE  PythonDataBase.Shares SET share_name = %s, high = %s, low = %s, volume = %s, trade = %s WHERE share_code = %s'''
        print(share.name, share.high, share.low, share.volume, 100, share.code)
        self.cursor.execute(sql, (share.name, float(share.high), float(share.low), int(share.volume), 100, share.code))
        self.change_commit()

    def change_commit(self):
        self.__db_helper.conn.commit()

    def close(self):
        self.cursor.close()
        self.__db_helper.close()
