import pymssql

class db():
    def __init__(self):
        db=pymssql.connect(server="127.0.0.1",user="sa",password="123456",database="student")
        self.cursor=db.cursor()

    def query(self,command):
        self.cursor.execute(command)