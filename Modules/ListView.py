# -*- coding: utf-8 -*-
# @Time    : 2020/3/9 10:37
# @Software: PyCharm
# @File    : ListView.py
# @Author  : DezeZhao
"""
显示列数据
"""
import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class ListView(QWidget):
    def __init__(self):
        super(ListView, self).__init__()
        self.setWindowTitle('QListView控件')
        self.resize(700, 500)

        layout = QVBoxLayout()
        listModel = QStringListModel()
        self.list = ['列表项1', '列表项2', '列表项3']
        listModel.setStringList(self.list)

        listview = QListView()
        listview.setModel(listModel)
        listview.clicked.connect(self.clicked)
        layout.addWidget(listview)
        self.setLayout(layout)

    def clicked(self, item):
        QMessageBox.information(self, "QListView", "您选择了" + self.list[item.row()])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = ListView()
    main.show()
    sys.exit(app.exec_())
