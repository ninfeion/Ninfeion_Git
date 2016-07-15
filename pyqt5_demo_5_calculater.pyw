# -*- coding: utf-8 -*-

from __future__ import division
import sys
from PyQt5 import QtCore
from math import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Mainwindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget') # ToolTip 1 富文本格式

        #btn = QPushButton('CAL', self)
        #btn.setToolTip('This is a <b>QPushButton</b> widget')   # ToolTip 2
        #btn.clicked.connect(self.calandupdateUi)
        #btn.resize(btn.sizeHint())
        #btn.move(50, 270)

        qbtn = QPushButton('Quit', self)
        qbtn.setToolTip('This is a <b>QuitButton</b> widget')
        #qbtn.clicked.connect(QCoreApplication.instance().quit) #QCoreApplication.instance().quit is a slot of QT modules internal,this signal also can connect a method which from user def.
        qbtn.clicked.connect(self.closeEvent)

        qbtn.resize(qbtn.sizeHint()) #sizeHint() return a default button size
        #qbtn.move(175, 270)

        self.browser = QTextBrowser()
        self.lineedit = QLineEdit("Type an expression and press Enter button")
        self.lineedit.selectAll()
        layout = QVBoxLayout()
        layout.addWidget(self.browser)
        layout.addWidget(self.lineedit)
        #layout.addWidget(btn)
        layout.addWidget(qbtn)

        self.setLayout(layout)
        self.lineedit.setFocus()
        self.lineedit.returnPressed.connect(self.calandupdateUi)

        self.setGeometry(300, 250, 300, 300)
        self.setWindowTitle('SUPER CALCULATER')
        self.setWindowIcon(QIcon('pyqt5_demo3_pic.png')) #QIcon accept a pic path

        # class QDesktopWidget provide to us the inf of my pc desktop, like the screen resolution
        self.center() # the method which move the window to center

        self.show()

    def calandupdateUi(self):
        try:
            text = self.lineedit.text()
            self.browser.append("%s = <b>%s</b>" % (text, eval(text)))
        except:
            self.browser.append(
                    "<font color=red>%s is invalid!</font>" % text)

    def closeEvent(self, QCloseEvent): # default method in the class
        reply = QMessageBox.question(self, 'Message',
                "Are you sure to quit?", QMessageBox.Yes |
                QMessageBox.No, QMessageBox.No) # Quit question messagebox set

        if reply == QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()

    def center(self):
        qr = self.frameGeometry() # create a frame from window
        cp = QDesktopWidget().availableGeometry().center() # calculate the screen center
        qr.moveCenter(cp) # move the center position of frame"qr" we created to position"cp"
        self.move(qr.topLeft()) # move the window to the frame"qr", and from topleft point to topleft

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculater = Mainwindow()
    sys.exit(app.exec_())