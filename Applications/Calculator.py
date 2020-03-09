# -*- coding: utf-8 -*-
# @Time    : 2020/3/9 12:58
# @Software: PyCharm
# @File    : Calculator.py
# @Author  : DezeZhao

import sys

from PyQt5.QtWidgets import *


class Calculator(QWidget):
    def __init__(self):
        super(Calculator, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('计算器')
        grid = QGridLayout()
        self.setLayout(grid)

        names = [
            'cls', 'Back', '', 'Close',
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        positions = [(i, j) for i in range(5) for j in range(4)]

        for position, name in zip(positions, names):
            if name == '':
                continue
            button = QPushButton(name)
            grid.addWidget(button, *position)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Calculator()
    main.show()
    sys.exit(app.exec_())
