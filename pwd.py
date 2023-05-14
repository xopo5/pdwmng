from PyQt5 import QtWidgets, QtGui, QtCore
# idkru.pythonanywhere.com/code/dezine

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.setWindowTitle('PasswordManager')
        self.resize(600, 480)

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
class PasswordWindow(QtWidgets.QWidget):
    def __init__(self,parent):
        super().__init__(parent)
        self.initUI()
    def initUI(self):
        v_layout = QtWidgets.QVBoxLayout()
        h1 = QtWidgets.QHBoxLayout()
        h2 = QtWidgets.QHBoxLayout()
        h3 = QtWidgets.QHBoxLayout()

        self.btn_edit = QtWidgets.QPushButton('Изменить')
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

        self.setLayout(v_layout)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    mw = MainWindow()
    mw.show()
    app.exec()
