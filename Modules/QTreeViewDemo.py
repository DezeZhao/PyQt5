# -*- coding: utf-8 -*-
# @Time    : 2020/3/8 20:39
# @Software: PyCharm
# @File    : QTreeViewDemo.py
# @Author  : DezeZhao
"""
QTreeView 控件与系统定制模式
Model装载数据
QDirModel
通常用来显示复杂的目录
直接显示系统目录
"""
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
if __name__ == '__main__':
    app = QApplication(sys.argv)
    model = QDirModel()
    tree = QTreeView()
    tree.setModel(model)
    tree.setWindowTitle('QTreeView演示')
    tree.resize(600,400)
    tree.show()
    sys.exit(app.exec_())