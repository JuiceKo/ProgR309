from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import *
import sys

from PyQt5.QtWidgets import QPushButton


class SubWindow(QWidget):
    def __init__(self):
        super(SubWindow, self).__init__()
        self.resize(400, 300)

        # Label
        self.label = QLabel(self)
        self.label.setText('Permet de convertir un nombre soit de Kelvion vers Celcius, '
                           'soit de Celcius vers Kelvin')


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        widget = QWidget()
        self.setCentralWidget(widget)

        grid = QGridLayout()
        widget.setLayout(grid)

        self.sub_window = SubWindow()

        Rien = QLabel("")
        Rien2 = QLabel("")
        TempLab = QLabel("Température")
        Conversion = QLabel("Conversion")
        DegLab = QLabel("°C")
        K = QLabel("K")
        self.__Temp = QLineEdit("")
        self.__result = QLineEdit("")
        Conv  = QPushButton("Convertir")
        quit = QPushButton("Quitter")
        self.__lab2 = QLabel("")
        self.__result.setReadOnly(True)

        what = QPushButton("?")

        self.__Choix = QComboBox(self)
        self.__Choix.addItem("°C -> K")
        self.__Choix.addItem("K -> °C")

        # Ajouter les composants au grid layout

        grid.addWidget(TempLab, 0, 0)
        grid.addWidget(self.__Temp, 0, 1)
        grid.addWidget(DegLab, 0, 2)
        grid.addWidget(Rien, 1, 1)
        grid.addWidget(Conv, 2, 1)
        grid.addWidget(self.__Choix, 2, 2)
        grid.addWidget(Rien2, 3, 0)
        grid.addWidget(Conversion, 4, 0)
        grid.addWidget(self.__result, 4, 1)
        grid.addWidget(K, 4, 2)
        grid.addWidget(what, 5, 3)

        Conv.clicked.connect(self.__actionOk)
        what.clicked.connect(self.sub_window.show)

        self.setWindowTitle("Une première fenêtre")
        self.setMinimumWidth(300)

    def __actionOk(self):
        Calcul = self.__Temp.Temp()
        self.__result.setText(f"Bonjour {Calcul}")

        """if self.__Choix.currentIndex() == 0:
            Calcul -= 273, 15
            self.__result.setText(Calcul)
        else:
            Calcul += 273, 15
            self.__result.setText(Calcul)"""

    """ def __edit(self):
            self.__lab2 = self.__text
            print("") """

    def __actionQuitter(self):
        QCoreApplication.exit(0)




    """def WHAT(self):"""





if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
