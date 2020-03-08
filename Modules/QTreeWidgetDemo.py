# -*- coding: utf-8 -*-
# @Time    : 2020/3/8 19:34
# @Software: PyCharm
# @File    : QTreeWidgetDemo.py
# @Author  : DezeZhao

"""
1.树控件QTreeWidget
2.树节点添加响应事件
3.树节点的修改，添加，删除
"""
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class QTreeWidgetDemo(QWidget):
    def __init__(self):
        super(QTreeWidgetDemo, self).__init__()
        self.resize(600, 600)

        self.setWindowTitle('树控件演示')
        self.tree = QTreeWidget()

        # 为树控件指定列数
        self.tree.setColumnCount(2)
        # 指定列标签
        self.tree.setHeaderLabels(['Key', 'Value'])

        root = QTreeWidgetItem(self.tree)
        root.setText(0, '根节点')
        root.setIcon(0, QIcon('../assets/icons/download.png'))
        self.tree.setColumnWidth(0, 300)

        # 添加子节点1
        child1 = QTreeWidgetItem(root)
        child1.setText(0, '子节点1')
        child1.setText(1, '子节点1的数据')
        child1.setIcon(0, QIcon('../assets/icons/download.png'))
        child1.setCheckState(0, Qt.Checked)

        # 添加子节点2
        child2 = QTreeWidgetItem(root)
        child2.setText(0, '子节点2')
        child2.setIcon(0, QIcon('../assets/icons/open.png'))

        # 添加子节点2的子节点
        child3 = QTreeWidgetItem(child2)
        child3.setText(0, '子节点2-1')
        child3.setText(1, '子节点2-1的值')
        child3.setIcon(0, QIcon('../assets/icons/save.png'))

        self.tree.expandAll()
        self.tree.clicked.connect(self.onTreeClicked)

        operatorLayout = QHBoxLayout()
        addBtn = QPushButton('添加节点')
        updateBtn = QPushButton('修改节点')
        deleteBtn = QPushButton('删除节点')

        operatorLayout.addWidget(addBtn)
        operatorLayout.addWidget(updateBtn)
        operatorLayout.addWidget(deleteBtn)

        addBtn.clicked.connect(self.addNode)
        updateBtn.clicked.connect(self.updateNode)
        deleteBtn.clicked.connect(self.deleteNode)

        mainLayout = QVBoxLayout()
        mainLayout.addLayout(operatorLayout)
        mainLayout.addWidget(self.tree)

        self.setLayout(mainLayout)

    def addNode(self):
        print('添加节点')
        item = self.tree.currentItem()
        print(item)
        node = QTreeWidgetItem(item)
        node.setText(0,'新节点')
        node.setText(1,'新值')

    def updateNode(self):
        print('修改节点')
        item = self.tree.currentItem()
        item.setText(0,'修改节点')
        item.setText(1,'值已被修改')

    def deleteNode(self):
        print('删除节点')
        item = self.tree.currentItem()
        root = self.tree.invisibleRootItem()
        for item in self.tree.selectedItems():
            # item.parent().removeChild(item) # 此时删除根节点会出错
            # item.parent()返回的是当前选中节点的父节点
            (item.parent() or root).removeChild(item)

    def onTreeClicked(self, index):
        item = self.tree.currentItem()
        print(index.row())
        print('key=%s , value=%s' % (item.text(0), item.text(1)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QTreeWidgetDemo()
    main.show()
    sys.exit(app.exec_())
