# -*- coding: utf-8 -*-
# @Time    : 2020/3/8 22:44
# @Software: PyCharm
# @File    : QStackWidgetDemo.py
# @Author  : DezeZhao
"""
堆栈窗口控件
QStackWidget
"""
import sys

from PyQt5.QtWidgets import *


class QStackWidgetDemo(QWidget):
    def __init__(self):
        super(QStackWidgetDemo, self).__init__()
        self.setWindowTitle('堆栈窗口演示')
        self.setGeometry(300, 50, 10, 10)

        # listWidget控件
        self.list = QListWidget()
        self.list.insertItem(0, '联系方式')
        self.list.insertItem(1, '个人信息')
        self.list.insertItem(2, '教育程度')

        self.stack1 = QWidget()
        self.stack2 = QWidget()
        self.stack3 = QWidget()

        self.tab1UI()
        self.tab2UI()
        self.tab3UI()

        self.stack = QStackedWidget()
        self.stack.addWidget(self.stack1)
        self.stack.addWidget(self.stack2)
        self.stack.addWidget(self.stack3)

        hbox = QHBoxLayout()
        hbox.addWidget(self.list)
        hbox.addWidget(self.stack)

        self.list.currentRowChanged.connect(self.display)

        self.setLayout(hbox)

    def display(self, index):
        self.stack.setCurrentIndex(index)

    def tab1UI(self):
        layout = QFormLayout()
        layout.addRow('姓名', QLineEdit())
        layout.addRow('地址', QLineEdit())
        # self.setStackText(0, '联系方式')
        self.stack1.setLayout(layout)

    def tab2UI(self):
        layout = QFormLayout()
        sex = QHBoxLayout()
        sex.addWidget(QRadioButton('男'))
        sex.addWidget(QRadioButton('女'))
        layout.addRow(QLabel('性别'), sex)
        layout.addRow('生日', QLineEdit())
        # self.setTabText(1, '个人详细信息')
        self.stack2.setLayout(layout)

    def tab3UI(self):
        layout = QHBoxLayout()
        layout.addWidget(QLabel('科目'))
        layout.addWidget(QCheckBox('物理'))
        layout.addWidget(QCheckBox('化学'))
        layout.addWidget(QCheckBox('数学'))
        # self.setTabText(2, '学科')
        self.stack3.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QStackWidgetDemo()
    main.show()
    sys.exit(app.exec_())
