# -*- coding: utf-8 -*-
# @Time    : 2020/3/1 20:21
# @Software: PyCharm
# @File    : QComBoxDemo.py
# @Author  : DezeZhao
"""
QComBox：
signal：currentIndexChanged  # 索引改变触发

"""
import sys

from PyQt5.QtWidgets import *


class QComBoxDemo(QWidget):
    def __init__(self):
        super(QComBoxDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('下拉列表演示')
        layout = QVBoxLayout()

        self.label = QLabel('请选择编程语言')
        self.cb = QComboBox()
        self.cb.addItem('C++')
        self.cb.addItem('Python')
        self.cb.addItems(['Java', 'C#', 'Go'])

        self.cb.currentIndexChanged.connect(self.selectionChanged)
        layout.addWidget(self.label)
        layout.addWidget(self.cb)

        self.setLayout(layout)

    def selectionChanged(self, idx):
        self.label.setText(self.cb.currentText())
        self.label.adjustSize()

        for count in range(self.cb.count()):
            print('item' + str(count) + "=" + self.cb.itemText(count))

        print('current index', idx, 'selection changed', self.cb.currentText())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QComBoxDemo()
    main.show()
    sys.exit(app.exec_())
