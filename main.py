# Интерфейс
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QComboBox, QLabel
from PyQt5.QtGui import QFont, QPixmap
from PyQt5 import QtCore
import matplotlib.pyplot as plt
from PyQt5 import uic


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.secondWin = None
        uic.loadUi('main.ui', self)
        a = plt.plot(list(range(1, 100)))
        plt.ylabel('Температура')
        plt.savefig('plot.png')
        self.label.setPixmap(QPixmap('plot.png').scaledToWidth(self.label.width()).scaledToHeight(self.label.height()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())
