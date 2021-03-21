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

        # Организация времени
        self.day.clear()
        self.day.addItems(map(str, range(1, month_per_day[int(self.month.currentText()) - 1] + 1)))
        func_changed = lambda *args, **kwargs: self.day.clear() or\
        self.day.addItems(map(str, range(1, month_per_day[int(self.month.currentText()) - 1] + 1)))
        self.month.currentIndexChanged.connect(func_changed)

        self.start.clicked.connect(self.click_start)

    def click_start(self):
        with open(f"cities/{self.city.currentText()}.json") as file:
            data = json.loads(file.read())

        year = int(self.year.currentText())
        month = int(self.month.currentText())
        day = int(self.day.currentText())
        plt.close()

        if self.graf_for.currentText() == 'год':
            plt.plot(data[(year - 1) * 365: year * 365])
        elif self.graf_for.currentText() == 'месяц':
            date_one = (year - 1) * 365 + sum(month_per_day[:month])
            plt.plot(data[date_one: date_one + month_per_day[month]])

        plt.ylabel('Температура')

        plt.savefig('plot.png')
        self.label.setPixmap(QPixmap('plot.png').scaledToWidth(self.label.width()).scaledToHeight(self.label.height()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())
