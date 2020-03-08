# -*- coding: utf-8 -*-
# @Time    : 2020/3/8 23:01
# @Software: PyCharm
# @File    : QScrollBarDemo.py
# @Author  : DezeZhao
"""
滚动条控件QScrollBar
1.通过滚动条值的变化控制其他控件的变化
2.通过滚动条值的变化控制控件位置变化
"""
import sys

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class QScrollBarDemo(QWidget):
    def __init__(self):
        super(QScrollBarDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('滚动条演示')
        hbox = QHBoxLayout()
        self.label = QLabel('拖动滚动条改变文字颜色')
        hbox.addWidget(self.label)
        self.scrollBar1 = QScrollBar()
        self.scrollBar1.setMaximum(255)
        self.scrollBar1.sliderMoved.connect(self.sliderMoved)

        self.scrollBar2 = QScrollBar()
        self.scrollBar2.setMaximum(255)
        self.scrollBar2.sliderMoved.connect(self.sliderMoved)

        self.scrollBar3 = QScrollBar()
        self.scrollBar3.setMaximum(255)
        self.scrollBar3.sliderMoved.connect(self.sliderMoved)

        hbox.addWidget(self.scrollBar1)
        hbox.addWidget(self.scrollBar2)
        hbox.addWidget(self.scrollBar3)

        self.scrollBar4 = QScrollBar()
        self.scrollBar4.setMaximum(255)
        self.scrollBar4.sliderMoved.connect(self.sliderMoved1)

        hbox.addWidget(self.scrollBar4)

        self.setLayout(hbox)

    def sliderMoved(self):
        print(self.scrollBar1.value())
        print(self.scrollBar2.value())
        print(self.scrollBar3.value())
        palette = QPalette()
        c = QColor(self.scrollBar1.value(),
                   self.scrollBar2.value(),
                   self.scrollBar3.value(), 255)
        palette.setColor(QPalette.Foreground, c)
        self.label.setPalette(palette)

    def sliderMoved1(self):
        self.label.move(self.label.x(), self.y() + self.scrollBar4.value())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QScrollBarDemo()
    main.show()
    sys.exit(app.exec_())
