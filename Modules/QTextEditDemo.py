# -*- coding: utf-8 -*-
# @Time    : 2020/3/1 17:21
# @Software: PyCharm
# @File    : QTextEditDemo.py
# @Author  : DezeZhao
import sys

from PyQt5.QtWidgets import *


class QTextEditDemo(QWidget):
    def __init__(self):
        super(QTextEditDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.textEdit = QTextEdit()
        self.setWindowTitle('QTextEdit控件演示')
        buttonText = QPushButton('显示文本')
        buttonHTML = QPushButton('显示HTML')
        buttontoHTML = QPushButton('获取HTML')
        buttontoText = QPushButton('获取文本')

        # self.resize(700, 500)

        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addWidget(buttonText)
        layout.addWidget(buttonHTML)
        layout.addWidget(buttontoText)
        layout.addWidget(buttontoHTML)

        self.setLayout(layout)

        buttonText.clicked.connect(self.onClick_Text)
        buttonHTML.clicked.connect(self.onClick_Html)
        buttontoText.clicked.connect(self.onClick_toText)
        buttontoHTML.clicked.connect(self.onClick_toHTML)

    def onClick_Text(self):
        self.textEdit.setPlainText('这是普通文本')

    def onClick_Html(self):
        self.textEdit.setHtml('<font size="16" color="green">这是HTML文本</font>')

    def onClick_toText(self):
        print(self.textEdit.toPlainText())

    def onClick_toHTML(self):
        print(self.textEdit.toHtml())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QTextEditDemo()
    main.show()
    sys.exit(app.exec_())
