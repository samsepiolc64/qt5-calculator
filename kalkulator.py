from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QLabel, QGridLayout
from PyQt5.QtWidgets import QLineEdit, QPushButton, QHBoxLayout

class Kalkulator(QWidget):
    def __init__(self, parent=None):
         super().__init__(parent)
         self.interfejs()

    def interfejs(self):
        #etykiety
        etykieta1 = QLabel("liczba 1:", self)
        etykieta2 = QLabel("liczba 2:", self)
        etykieta3 = QLabel("wynik:", self)

        # jednoliniowe pola edycyjne
        self.liczba1Edt = QLineEdit()
        self.liczba2Edt = QLineEdit()
        self.wynikEdt = QLineEdit()

        self.wynikEdt.readonly = True
        self.wynikEdt.setToolTip("wpisz liczby i wybierz dzialanie")

        # przyciski
        dodajBtn = QPushButton("&Dodaj", self)
        odejmijBtn = QPushButton("&Odejmij", self)
        dzielBtn = QPushButton("&Dziel", self)
        mnozBtn = QPushButton("&Mnóż", self)
        koniecBtn = QPushButton("&Koniec", self)
        koniecBtn.resize(koniecBtn.sizeHint())

        # przypisanie widgetow do ukladu tabelarycznego
        ukladT = QGridLayout()
        ukladT.addWidget(etykieta1, 0, 0)
        ukladT.addWidget(etykieta2, 0, 1)
        ukladT.addWidget(etykieta3, 0, 2)
        ukladT.addWidget(self.liczba1Edt, 1, 0)
        ukladT.addWidget(self.liczba2Edt, 1, 1)
        ukladT.addWidget(self.wynikEdt, 1, 2)
        ukladH = QHBoxLayout()
        ukladH.addWidget(dodajBtn)
        ukladH.addWidget(odejmijBtn)
        ukladH.addWidget(dzielBtn)
        ukladH.addWidget(mnozBtn)

        ukladT.addLayout(ukladH, 2, 0, 1, 3)
        ukladT.addWidget(koniecBtn, 3, 0, 1, 3)

        # przypisanie ukladu tabelarycznego do okna
        self.setLayout(ukladT)

        self.setGeometry(120, 120, 300, 100)
        self.setWindowIcon(QIcon('kalkulator.png'))
        self.setWindowTitle("Prosty kalkulator")
        self.show()

if __name__ == '__main__':
    import sys

    app=QApplication(sys.argv)
    okno = Kalkulator()
    sys.exit(app.exec_())