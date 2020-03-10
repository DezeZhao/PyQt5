# -*- coding: utf-8 -*-
# @Time    : 2020/3/10 18:13
# @Software: PyCharm
# @File    : OverrideSlot.py
# @Author  : DezeZhao
"""
覆盖槽函数
"""
import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class OverrideSlot(QWidget):
    def __init__(self):
        super(OverrideSlot, self).__init__()
        self.setWindowTitle('Override演示')

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()
        elif e.key() == Qt.Key_Alt:
            self.setWindowTitle('ALT pressed')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = OverrideSlot()
    main.show()
    sys.exit(app.exec_())
