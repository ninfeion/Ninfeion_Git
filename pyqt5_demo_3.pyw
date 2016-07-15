# -*- coding: utf-8 -*-

"""
THIS EXAMPLE SHOWS AN ICON IN THE TITLEBAR OF THE WINDOW
"""

import sys
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import QIcon

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300) # the method combine resize() and move(), the first and second arguement set up window x,y position,the third and fourth set the width and heigth.
        self.setWindowTitle('Icon')

        self.setWindowIcon(QIcon('pyqt5_demo3_pic.png')) # The main method in the chapter

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())