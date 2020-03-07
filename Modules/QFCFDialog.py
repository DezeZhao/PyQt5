# -*- coding: utf-8 -*-
# @Time    : 2020/3/7 22:36
# @Software: PyCharm
# @File    : QFCFDialog.py
# @Author  : DezeZhao
"""
字体对话框
QFontDialog
颜色对话框
QColorDialog
文件对话框
QFileDialog
"""
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class QFCFDialog(QWidget):
    def __init__(self):
        super(QFCFDialog, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('字体(Font)颜色(Color)文件(File)对话框演示')
        self.resize(700, 500)
        layout = QVBoxLayout()

        self.label = QLabel('字体(Font)颜色(Color)文件(File)演示')
        layout.addWidget(self.label)

        self.fontBtn = QPushButton('选择字体')
        self.fontBtn.clicked.connect(self.getFont)
        layout.addWidget(self.fontBtn)

        self.colorBtn = QPushButton('选择颜色')
        self.colorBtn.clicked.connect(self.getColor)
        layout.addWidget(self.colorBtn)

        self.bgColorBtn = QPushButton('设置背景颜色')
        self.bgColorBtn.clicked.connect(self.getBgColor)
        layout.addWidget(self.bgColorBtn)

        self.imgBtn = QPushButton('加载图片')
        self.imgBtn.clicked.connect(self.loadImage)
        layout.addWidget(self.imgBtn)

        self.imgLabel = QLabel()
        layout.addWidget(self.imgLabel)

        self.txtBtn = QPushButton('加载文本')
        self.txtBtn.clicked.connect(self.loadText)
        layout.addWidget(self.txtBtn)

        self.contents = QTextEdit()
        layout.addWidget(self.contents)

        self.setLayout(layout)

    def getFont(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.label.setFont(font)

    def getColor(self):
        # getcolor函数不返回ok只有颜色值color
        color = QColorDialog.getColor()
        # 设置文字颜色
        p = QPalette()
        p.setColor(QPalette.WindowText, color)
        self.label.setPalette(p)

    def getBgColor(self):
        # getcolor函数不返回ok只有颜色值color
        color = QColorDialog.getColor()
        # 设置背景颜色
        p = QPalette()
        p.setColor(QPalette.Window, color)
        self.label.setAutoFillBackground(True)
        self.label.setPalette(p)

    # QFileDialog就是系统对话框的那个类
    # 第一个参数是上下文
    # 第二个参数是弹框的名字
    # 第三个参数是开始打开的路径(i.e 'C:\\')
    # 第四个参数是需要的格式
    def loadImage(self):
        fname, _ = QFileDialog.getOpenFileName(self, '打开文件', '.', '图像文件(*.jpg *.png)')
        self.imgLabel.setPixmap(QPixmap(fname))

    def loadText(self):
        dialog = QFileDialog()
        # 初始化这个实例，设置一些基本属性
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setFilter(QDir.Files)
        # 当选择器关闭的时候
        if dialog.exec():
            # 拿到所选择的的文件
            fnames = dialog.selectedFiles()
            f = open(fnames[0], 'r')
            with f:
                data = f.read()
                self.contents.setText(data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QFCFDialog()
    main.show()
    sys.exit(app.exec_())
