# Интерфейс
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap
import matplotlib.pyplot as plt
from PyQt5 import uic
import json
from MainForm import Ui_MainWindow
from requester import getPredictionForDay, getPredictionForMonth, getPredictionForYear


month_per_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.set_time()

    def set_time(self):  # Организация времени
        self.dayComboBox.clear()
        self.dayComboBox.addItems(map(str, range(1, month_per_day[int(self.monthComboBox.currentText()) - 1] + 1)))
        func_changed = lambda *args, **kwargs: self.dayComboBox.clear() or \
                                               self.dayComboBox.addItems(map(str, range(1, month_per_day[
                                                   int(self.monthComboBox.currentText()) - 1] + 1)))
        self.monthComboBox.currentIndexChanged.connect(func_changed)

        self.showGraphicButton.clicked.connect(self.show_graphic)

    def show_graphic(self):
        month = int(self.monthComboBox.currentText())
        day = int(self.dayComboBox.currentText())
        city = self.cityComboBox.currentText()

        data_for_year = getPredictionForYear(city)
        data_for_month = getPredictionForMonth(city, month)
        data_for_day = getPredictionForDay(city, day)

        day_in_json = month * day

        plt.close()

        if self.graphicFor.currentText() == 'год':
            plt.plot(data_for_year)
        elif self.graphicFor.currentText() == 'месяц':
            plt.plot(data_for_month)
        elif self.graphicFor.currentText() == 'день':
            self.graphicLabel.clear()
            s = "{:10.2f}".format(data_for_day[0])
            self.graphicLabel.setText(s)
            return

        plt.ylabel('Температура')

        plt.savefig('plot.png')
        width, height = self.graphicLabel.width(), self.graphicLabel.height()
        self.graphicLabel.setPixmap(QPixmap('plot.png').scaledToWidth(width).scaledToHeight(height))


app = QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()
sys.exit(app.exec_())
