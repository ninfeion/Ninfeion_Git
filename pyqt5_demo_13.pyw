# -*- coding: utf-8 -*-

"""
RECEIVE DATA FROM A QINPUTDIALOG DIALOG.
"""

import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QInputDialog, QApplication,  QColorDialog, QFrame
from PyQt5.QtGui import QColor

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.btn = QPushButton('Dialog', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)

        #col = QColor(0, 0, 0)
        #self.cbtn = QPushButton('Color choose', self)
        #self.cbtn.move(20, 50)
        #self.cbtn.clicked.connect(self.showColorChooseDialog())

        #self.frm = QFrame(self)
        #self.frm.setStyleSheet("QWidget { backgroud-color: %s }" % col.name())
        #self.frm.setGeometry(130, 22, 100, 100)

        self.le = QLineEdit('?', self)
        self.le.move(130, 22)

        self.setGeometry(300, 300, 290, 250)
        self.setWindowTitle('Input dialog')
        self.show()

    def showDialog(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your name:') #return str and bool value
        if ok:
            self.le.setText(str(text))

    #def showColorChooseDialog(self):
        #col = QColorDialog.getColor()

        #if col.isValid():
            #self.frm.setStyleSheet("QWidget { background-color: %s }" % col.name())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())