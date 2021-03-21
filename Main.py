# Интерфейс
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap
import matplotlib.pyplot as plt
from PyQt5 import uic
import json
from MainForm import Ui_MainWindow


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
        with open(f"cities/{self.cityComboBox.currentText()}.json") as file:
            data = json.loads(file.read())

        year = 1
        month = int(self.monthComboBox.currentText())
        day = int(self.dayComboBox.currentText())
        plt.close()

        if self.graphicFor.currentText() == 'год':
            plt.plot(data[(year - 1) * 365: year * 365])
        elif self.graphicFor.currentText() == 'месяц':
            date_one = (year - 1) * 365 + sum(month_per_day[:month])
            plt.plot(data[date_one: date_one + month_per_day[month]])

        plt.ylabel('Температура')

        plt.savefig('plot.png')
        width, height = self.graphicLabel.width(), self.graphicLabel.height()
        self.graphicLabel.setPixmap(QPixmap('plot.png').scaledToWidth(width).scaledToHeight(height))


app = QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()
sys.exit(app.exec_())
