from enum import Enum

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QMessageBox, QTableWidgetItem
import sys


class MainWindow(QWidget):
    count = 0
    def __init__(self):
        super().__init__()
        uic.loadUi('tel.ui', self)
        self.buttonAdd.clicked.connect(self.foo)

    def foo(self, count):
        try:
            rows = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rows)
            self.tableWidget.setItem(rows, 0, QTableWidgetItem(self.lineName.text()))
            self.tableWidget.setItem(rows, 1, QTableWidgetItem(self.lineNumber.text()))


        except Exception:
            QMessageBox.Abort(self, "Ошибка", "Неверные данные")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())
