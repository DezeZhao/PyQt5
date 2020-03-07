# -*- coding: utf-8 -*-
# @Time    : 2020/3/7 17:52
# @Software: PyCharm
# @File    : QSpinBoxDemo.py
# @Author  : DezeZhao

"""


"""
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class QSpinBoxDemo(QWidget):
    def __init__(self):
        super(QSpinBoxDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('计数器控件演示')
        self.resize(300, 200)

        layout = QVBoxLayout()

        self.label = QLabel('当前值')
        self.label.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.label)

        self.sb = QSpinBox()
        self.sb.setValue(17)
        self.sb.setRange(9,30)
        self.sb.setSingleStep(3)  #步长为3
        layout.addWidget(self.sb)
        self.sb.valueChanged.connect(self.valueChange)

        self.setLayout(layout)

    def valueChange(self):
        self.label.setText('当前值：' + str(self.sb.value()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QSpinBoxDemo()
    main.show()
    sys.exit(app.exec_())
