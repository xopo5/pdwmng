from PyQt5 import QtWidgets, QtGui, QtCore
import keyring
import json
# idkru.pythonanywhere.com/code/dezine

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.setWindowTitle('PasswordManager')
        self.resize(600, 480)

        self.db = DataBase(  )

        self.add_pwd_win = PasswordWindow(self.db,self)
        self.btn_add_pwd.clicked.connect(self.add_pwd_win.show)


    def initUI(self):
        self.btn_add_pwd = QtWidgets.QPushButton('Добавить')
        self.pwd_list = QtWidgets.QListWidget()

        h_layout = QtWidgets.QHBoxLayout()
        v_layout = QtWidgets.QVBoxLayout()

        h_layout.addStretch(6)
        h_layout.addWidget(self.btn_add_pwd, stretch=2)

        v_layout.addLayout(h_layout)
        v_layout.addWidget(self.pwd_list)

        self.setLayout(v_layout)
    def update_list(self):
        self.pwd_list.clear()
        data = self.db.get_list()
        self.pwd_list.addItems(data)
class PasswordWindow(QtWidgets.QWidget):
    def __init__(self,db,mw):
        super().__init__()
        self.db = db
        self.mw = mw
        self.initUI()
    def initUI(self):
        v_layout = QtWidgets.QVBoxLayout()
        h1 = QtWidgets.QHBoxLayout()
        h2 = QtWidgets.QHBoxLayout()
        h3 = QtWidgets.QHBoxLayout()

        self.btn_save = QtWidgets.QPushButton('Сохранить')
        self.btn_close = QtWidgets.QPushButton('Закрыть')
        self.btn_copy = QtWidgets.QPushButton('Скопировать')
        
        self.service_edit = QtWidgets.QLineEdit()
        self.login_edit = QtWidgets.QLineEdit()
        self.pwd_edit = QtWidgets.QLineEdit()

        self.pwd_edit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        service_lbl = QtWidgets.QLabel('Название сервиса')
        login_lbl = QtWidgets.QLabel('Название логина')
        pwd_lbl = QtWidgets.QLabel('Пароль')

        h1.addWidget(service_lbl,stretch=3)
        h1.addWidget(self.service_edit,stretch=5)
        
        h2.addWidget(login_lbl,stretch=3)
        h2.addWidget(self.login_edit,stretch=5)
        
        h3.addWidget(pwd_lbl,stretch=3)
        h3.addWidget(self.pwd_edit,stretch=5)
        
        v_layout.addLayout(h1)
        v_layout.addLayout(h2)
        v_layout.addLayout(h3)
        v_layout.addWidget(self.btn_save, alignment = QtCore.Qt.AlignCenter)

        self.setLayout(v_layout)
    def add_password(self):
        service = self.service_edit.text()
        login = self.login_edit.text()
        password = self.pwd_edit.text()
        self.db.set_password(service,login,password)
        self.service_edit.clear()
        self.login_edit.clear()
        self.pwd_edit.clear()
        self.hide()
        self.mw.update_list()
class DataBase():
    def __init__(self):
        self.filename = 'services.json'
        try:
            with open(self.filename,'r') as file:
                self.data = json.load(file)
        except:
            open(self.filename,'w')
            self.data = dict()
    def set_password(self,service,login,password):
        keyring.set_password(service,login,password)
        self.data[service] = login
        with open(self.filename,'w') as file:
            json.dump(self.data,file)
    def get_password(self,service,login):
        return keyring.get_password(service,login)
    def get_list(self):
        result = []  
        for key in self.data:
            text = key+ ' | '+ self.data[key]
            result.append(text)
        return text

 
if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    mw = MainWindow()
    mw.show()
    app.exec()
