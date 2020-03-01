# -*- coding: utf-8 -*-
# @Time    : 2020/2/29 23:44
# @Software: PyCharm
# @File    : QuitApplication.py
# @Author  : DezeZhao
import sys

from PyQt5.QtWidgets import QApplication, QHBoxLayout, QMainWindow, QPushButton, QWidget


class QuitApplication(QMainWindow):
    def __init__(self):
        super(QuitApplication, self).__init__()
        self.resize(500, 700)
        self.setWindowTitle('退出应用程序')

        self.button = QPushButton('退出应用程序')
        self.button.clicked.connect(self.onClick_Button)

        layout = QHBoxLayout()
        layout.addWidget(self.button)

        mainForm = QWidget()
        mainForm.setLayout(layout)

        self.setCentralWidget(mainForm)

    def onClick_Button(self):
        sender = self.sender()
        print(sender.text())  # 按钮上的字体
        app1 = QApplication.instance()
        app1.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QuitApplication()
    main.show()
    sys.exit(app.exec_())
