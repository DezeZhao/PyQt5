# -*- coding: utf-8 -*-
# @Time    : 2020/3/8 12:03
# @Software: PyCharm
# @File    : ClipBoard.py
# @Author  : DezeZhao

import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class ClipBoard(QDialog):
    def __init__(self):
        super(ClipBoard, self).__init__()
        textCopyBtn = QPushButton('复制文本')
        textPasteBtn = QPushButton('粘贴文本')

        htmlCopyBtn = QPushButton('复制HTML')
        htmlPasteBtn = QPushButton('粘贴HTML')

        imageCopyBtn = QPushButton('复制图像')
        imagePasteBtn = QPushButton('粘贴图像')

        self.textLabel = QLabel('默认文本')
        self.imageLabel = QLabel()
        self.imageLabel.setPixmap(QPixmap('../assets/images/pythonlogo.png'))

        layout = QGridLayout()
        layout.addWidget(textCopyBtn, 0, 0)
        layout.addWidget(imageCopyBtn, 0, 1)
        layout.addWidget(htmlCopyBtn, 0, 2)
        layout.addWidget(textPasteBtn, 1, 0)
        layout.addWidget(imagePasteBtn, 1, 1)
        layout.addWidget(htmlPasteBtn, 1, 2)

        layout.addWidget(self.textLabel, 2, 0, 1, 2)
        layout.addWidget(self.imageLabel, 2, 2)

        textCopyBtn.clicked.connect(self.copyText)
        textPasteBtn.clicked.connect(self.pasteText)
        imageCopyBtn.clicked.connect(self.copyImage)
        imagePasteBtn.clicked.connect(self.pasteImage)
        htmlCopyBtn.clicked.connect(self.copyHtml)
        htmlPasteBtn.clicked.connect(self.pasteHtml)

        self.setWindowTitle('剪贴板演示')
        self.setLayout(layout)

    def copyText(self):
        clipboard = QApplication.clipboard()
        clipboard.setText('herllo world')

    def pasteText(self):
        clipboard = QApplication.clipboard()
        self.textLabel.setText(clipboard.text())

    def copyImage(self):
        clipboard = QApplication.clipboard()
        clipboard.setPixmap(QPixmap('../assets/images/pythonlogo.png'))

    def pasteImage(self):
        clipboard = QApplication.clipboard()
        self.imageLabel.setPixmap(clipboard.pixmap())

    def copyHtml(self):
        mimeData = QMimeData()
        mimeData.setHtml('<b>cdsjcndsjcbjdbj<font color=red>cbsjdbjs</font></b>')
        clipboard = QApplication.clipboard()
        clipboard.setMimeData(mimeData)

    def pasteHtml(self):
        clipboard = QApplication.clipboard()
        mimeData = clipboard.mimeData()
        if mimeData.hasHtml():
            self.textLabel.setText(mimeData.html())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = ClipBoard()
    main.show()
    sys.exit(app.exec_())
