# -*- coding: utf-8 -*-
# @Time    : 2020/3/7 17:23
# @Software: PyCharm
# @File    : QSliderDemo.py
# @Author  : DezeZhao

"""
滑块控件QSlider
"""
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class QSliderDemo(QWidget):
    def __init__(self):
        super(QSliderDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('SLider demo')
        self.resize(300, 200)
        layout = QVBoxLayout()

        self.label = QLabel('你好PyQt5')
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(12)
        self.slider.setMaximum(48)
        self.slider.setSingleStep(3)
        self.slider.setValue(18)
        self.slider.setTickPosition(QSlider.TicksBelow)
        # 设置刻度间隔
        self.slider.setTickInterval(6)
        layout.addWidget(self.slider)
        self.slider.valueChanged.connect(self.valueChange)
        self.setLayout(layout)

    def valueChange(self):
        print('current value:%s' % self.slider.value())
        size = self.slider.value()
        self.label.setFont(QFont('Arial', size))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QSliderDemo()
    main.show()
    sys.exit(app.exec_())
