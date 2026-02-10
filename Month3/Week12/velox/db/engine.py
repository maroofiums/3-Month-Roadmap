import sqlite3

class VeloxDB:
    def __init__(self, name="db.sqlite3"):
        self.conn = sqlite3.connect(name)
        self.cursor = self.conn.cursor()

    def execute(self, sql):
        self.cursor.execute(sql)
        self.conn.commit()
