# -*- coding: utf-8 -*-
# @Time    : 2020/3/1 19:58
# @Software: PyCharm
# @File    : QCheckBoxDemo.py
# @Author  : DezeZhao
"""
复选框控件
未选中：0
半选中：1
选中 ：2

signal:
stateChanged
"""
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class QCheckBoxDemo(QWidget):
    def __init__(self):
        super(QCheckBoxDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('复选框演示')
        layout = QHBoxLayout()

        self.box1 = QCheckBox('复选框1')
        self.box1.setChecked(True)
        self.box1.stateChanged.connect(lambda: self.ChecboxState(self.box1))
        layout.addWidget(self.box1)

        self.box2 = QCheckBox('复选框2')
        self.box2.stateChanged.connect(lambda: self.ChecboxState(self.box2))
        layout.addWidget(self.box2) #

        self.box3 = QCheckBox('半选中')
        self.box3.stateChanged.connect(lambda: self.ChecboxState(self.box3))
        self.box3.setTristate(True)
        self.box3.setCheckState(Qt.PartiallyChecked)
        layout.addWidget(self.box3)

        self.setLayout(layout)

    def ChecboxState(self, cb):
        chaeck1Status = self.box1.text() + ', is Checked=' + str(self.box1.isChecked()) + '.checkState=' + str(self.box1.checkState())
        chaeck2Status = self.box2.text() + ', is Checked=' + str(self.box2.isChecked()) + '.checkState=' + str(self.box2.checkState())
        chaeck3Status = self.box3.text() + ', is Checked=' + str(self.box3.isChecked()) + '.checkState=' + str(self.box3.checkState())
        print(chaeck1Status + '\n'+chaeck2Status +'\n'+ chaeck3Status)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QCheckBoxDemo()
    main.show()
    sys.exit(app.exec_())
