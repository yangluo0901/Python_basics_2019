import pymysql


class DbManager(object):

    def __init__(self, host, user, port):
        self.conn = pymysql.connect(host=host, user=user, port=port, passwd="root", charset="utf8")

    def createdb(self):



    def addentry(self):