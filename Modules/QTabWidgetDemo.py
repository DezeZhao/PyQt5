# -*- coding: utf-8 -*-
# @Time    : 2020/3/8 20:46
# @Software: PyCharm
# @File    : QTabWidgetDemo.py
# @Author  : DezeZhao
"""
选项卡控件
放多个页面
"""
import sys

from PyQt5.QtWidgets import *


class QTabWidgetDemo(QTabWidget):  # 整个窗口作为一个选项卡
    def __init__(self):
        super(QTabWidgetDemo, self).__init__()
        self.setWindowTitle('选项卡控件')
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()  # 显示控件的窗口为Widget

        self.addTab(self.tab1, '选项卡1')
        self.addTab(self.tab2, '选项卡2')
        self.addTab(self.tab3, '选项卡3')

        self.tab1UI()
        self.tab2UI()
        self.tab3UI()
        self.resize(500, 500)

    def tab1UI(self):
        layout = QFormLayout()
        layout.addRow('姓名', QLineEdit())
        layout.addRow('地址', QLineEdit())
        self.setTabText(0, '联系方式')
        self.tab1.setLayout(layout)

    def tab2UI(self):
        layout = QFormLayout()
        sex = QHBoxLayout()
        sex.addWidget(QRadioButton('男'))
        sex.addWidget(QRadioButton('女'))
        layout.addRow(QLabel('性别'), sex)
        layout.addRow('生日', QLineEdit())
        self.setTabText(1, '个人详细信息')
        self.tab2.setLayout(layout)

    def tab3UI(self):
        layout = QHBoxLayout()
        layout.addWidget(QLabel('科目'))
        layout.addWidget(QCheckBox('物理'))
        layout.addWidget(QCheckBox('化学'))
        layout.addWidget(QCheckBox('数学'))
        self.setTabText(2, '学科')
        self.tab3.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QTabWidgetDemo()
    main.show()
    sys.exit(app.exec_())
