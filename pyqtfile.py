import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication, QLineEdit, QVBoxLayout
from PyQt5 import uic
import random

class Password(QMainWindow):
    def __init__(self):
        super().__init__()
        self.clicked_btn = set()


        self.let = 'qwertyuiopasdfghjklzxcvbnm'
        self.num = '1234567890'
        self.spec_sim = '%*)?@#$_'
        self.let_big = 'QWERTYUIOPASDFGHJKLZXCVBNM'
        self.symbol = [self.let, self.num, self.spec_sim, self.let_big]

        self.initUI()


    def initUI(self):
        uic.loadUi('genpassword.ui', self)

        self.az.clicked.connect(self.clicked)
        self.num.clicked.connect(self.clicked)
        self.spec.clicked.connect(self.clicked)
        self.AZ.clicked.connect(self.clicked)
        self.OK.clicked.connect(self.final)

        self.setWindowTitle('пароль')
        self.resize(270, 256)
        self.show()

    def clicked(self):
        if self.az.isChecked():
            self.clicked_btn.add(1)
        if self.num.isChecked():
            self.clicked_btn.add(2)
        if self.spec.isChecked():
            self.clicked_btn.add(3)
        if self.AZ.isChecked():
            self.clicked_btn.add(4)

    def itog(self):
        self.it = ''
        for i in self.clicked_btn:
            self.it += self.symbol[int(i)-1]
        return self.it

    def genetare_password(self, symbol, length):
        for s in range(length):
            r = random.randint(0, len(symbol) - 1)
            yield symbol[r]

    def password_itog(self, f):
        password = ''
        for i in f:
            password += i

        return password

    def __zero__(self):
        self.length.setText('')
        self.az.setChecked(False)
        self.num.setChecked(False)
        self.spec.setChecked(False)
        self.AZ.setChecked(False)
        self.clicked_btn = set()

    def final(self):
        try:
            if int(self.length.toPlainText()) <= 18:
                self.i = self.itog()
                self.g = self.genetare_password(self.i, int(self.length.toPlainText()))
                self.pswrd = self.password_itog(self.g)

                self.password.setText(f'<b>{self.pswrd}</b>')
                self.__zero__()

            else:
                self.password.setText(f'<b>Ошибка!<br> Попробуйте снова!</b>')
                self.__zero__()

        except:
            self.password.setText(f'<b>Ошибка!<br> Попробуйте снова!</b>')
            self.__zero__()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Password()
    sys.exit(app.exec_())