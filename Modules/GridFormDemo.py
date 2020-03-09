# -*- coding: utf-8 -*-
# @Time    : 2020/3/9 15:38
# @Software: PyCharm
# @File    : GridFormDemo.py
# @Author  : DezeZhao
"""
跨行跨列设计表单
某个控件占用多列或多行
"""
import sys

from PyQt5.QtWidgets import *


class GridFromDemo(QWidget):
    def __init__(self):
        super(GridFromDemo, self).__init__()
        self.setWindowTitle('栅格布局：表单设计')

        # self.resize(500, 500)
        wg = QWidget(self)  # 整个窗口为wg 绝对布局
        vlayout = QVBoxLayout(wg)  # 将垂直布局放在窗口中

        grid = QGridLayout()
        form = QFormLayout()

        titleLabel = QLabel('标题')
        authorLabel = QLabel('作者')
        contentsLabel = QLabel('内容')
        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        contentsEdit = QTextEdit()
        plan1 = QLabel('QGridLayout achieve')

        titleLabel1 = QLabel('标题')
        authorLabel1 = QLabel('作者')
        contentsLabel1 = QLabel('内容')
        titleEdit1 = QLineEdit()
        authorEdit1 = QLineEdit()
        contentsEdit1 = QTextEdit()
        plan2 = QLabel('QFormLayout achieve')

        grid.addWidget(plan1, 0, 0, 1, 2)
        grid.addWidget(titleLabel, 1, 0)
        grid.addWidget(titleEdit, 1, 1)
        grid.addWidget(authorLabel, 2, 0)
        grid.addWidget(authorEdit, 2, 1)
        grid.addWidget(contentsLabel, 3, 0)
        grid.addWidget(contentsEdit, 3, 1, 5, 1)

        form.addRow(plan2)
        form.addRow(titleLabel1, titleEdit1)
        form.addRow(authorLabel1, authorEdit1)
        form.addRow(contentsLabel1, contentsEdit1)

        vlayout.addLayout(grid)
        vlayout.addLayout(form)

        self.setLayout(vlayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = GridFromDemo()
    main.show()
    sys.exit(app.exec_())
