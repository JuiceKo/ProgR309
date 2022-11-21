from PyQt5.QtWidgets import *
from PyQt5.QtCore import QCoreApplication
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        widget = QWidget()
        self.setCentralWidget(widget)

        grid = QVBoxLayout()
        widget.setLayout(grid)

        lab = QLabel("Saisir votre nom")
        self.__text = QLineEdit()
        ok = QPushButton("Ok")
        quit = QPushButton("Quitter")
        self.__lab2 = QLabel("")

        # Ajouter les composants au grid layout

        grid.addWidget(lab)
        grid.addWidget(self.__text)
        grid.addWidget(ok)
        grid.addWidget(self.__lab2)
        grid.addWidget(quit)

        ok.clicked.connect(self.__actionOk)
        """self.__text.returnPressed.connect(self.__edit)"""
        quit.clicked.connect(self.__actionQuitter)


        self.setWindowTitle("Une première fenêtre")

    def __actionOk(self):
        prenom = self.__text.text()
        self.__lab2.setText(prenom)

        """   def __edit(self):
        self.__lab2 = self.__text
        print("") """

    def __actionQuitter(self):
        QCoreApplication.exit(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
