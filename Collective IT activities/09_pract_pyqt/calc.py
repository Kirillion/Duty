from enum import Enum

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class Operation(Enum):
    plus = 1
    minus = 2
    mul = 3
    div = 4
    power = 5


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('calc.ui', self)
        self.delet.clicked.connect(lambda: self.foo(Operation.div))
        self.minus.clicked.connect(lambda: self.foo(Operation.minus))
        self.plus.clicked.connect(lambda: self.foo(Operation.plus))
        self.multiplue.clicked.connect(lambda: self.foo(Operation.mul))
        self.stepen.clicked.connect(lambda: self.foo(Operation.power))

    def foo(self, op):
        try:
            arg1 = float(self.FirstText.text())
            arg2 = float(self.SecondText.text())
            if op == Operation.plus:
                result = arg1 + arg2
                self.outText.setText(str(result))
            if op == Operation.div:
                result = arg1 / arg2
                self.outText.setText(str(result))
            if op == Operation.minus:
                result = arg1 - arg2
                self.outText.setText(str(result))
            if op == Operation.mul:
                result = arg1 * arg2
                self.outText.setText(str(result))
            if op == Operation.power:
                result = arg1 ** arg2
                self.outText.setText(str(result))
        except Exception:
            self.outText.setText('Invalid arguments')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.setWindowTitle("Калькулятор")
    ex.show()
    sys.exit(app.exec_())