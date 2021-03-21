# Интерфейс
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QComboBox, QLabel, QComboBox
from PyQt5.QtGui import QFont, QPixmap
from PyQt5 import QtCore
import matplotlib.pyplot as plt
from PyQt5 import uic
import json
import numpy as np

month_per_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.secondWin = None
        uic.loadUi('main.ui', self)

        with open("cities/Западный.json") as file:
            data = json.loads(file.read())
        plt.plot([np.median(j) for j in [data[i * 365: (i + 1) * 365] for i in range(len(data) // 365)]])
        plt.ylabel('Температура')
        plt.savefig('plot.png')
        self.label.setPixmap(QPixmap('plot.png').scaledToWidth(self.label.width()).scaledToHeight(self.label.height()))

        # Организация времени
        self.day.clear()
        self.day.addItems(map(str, range(1, month_per_day[int(self.month.currentText()) - 1] + 1)))
        func_changed = lambda *args, **kwargs: self.day.clear() or\
        self.day.addItems(map(str, range(1, month_per_day[int(self.month.currentText()) - 1] + 1)))
        self.month.currentIndexChanged.connect(func_changed)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())
