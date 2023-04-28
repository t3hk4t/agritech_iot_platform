import sqlite3


class Model:

    def __init__(self):
        self.con = None
        self.cur = None

    def getMyData(self):
        return "test"
