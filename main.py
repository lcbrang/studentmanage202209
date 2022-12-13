import sys
from PyQt5.QtWidgets import QApplication,QWidget
from login import Ui_login
from home import Ui_stuhome
from mysqldb import *


class Login(QWidget):
    def __init__(self):
        super(Login, self).__init__()
        self.login_ui=Ui_login()
        self.login_ui.setupUi(self)
        self.login_ui.login.clicked.connect(self.login)
        self.show()

    def login(self):
        self.db = db()
        command = f"select * from account where id='{self.login_ui.username.text()}' and password='{self.login_ui.password.text()}'"
        self.db.query(command)
        if self.db.cursor.fetchall():
            login.close()
            home.show()
        else:
            login.login_ui.label_5.setText("密码错误")
            login.show()


class Home(QWidget):
    def __init__(self):
        super(Home, self).__init__()
        self.home_ui=Ui_stuhome()
        self.home_ui.setupUi(self)


if __name__ == '__main__':
    app=QApplication(sys.argv)
    login=Login()
    home=Home()
    sys.exit(app.exec_())