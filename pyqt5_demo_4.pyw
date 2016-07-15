# -*- coding: utf-8 -*-

"""
THIS EXAMPLE SHOWS A TOOLTIP ON A WINDOW AND A BOTTON
"""

import  sys
from PyQt5.QtWidgets import QDesktopWidget,QWidget, QToolTip, QPushButton, QApplication, QMessageBox
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import QCoreApplication # import some method like quit

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget') # ToolTip 1 富文本格式

        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')   # ToolTip 2
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        qbtn = QPushButton('Quit', self)
        qbtn.setToolTip('This is a <b>QuitButton</b> widget')
        #qbtn.clicked.connect(QCoreApplication.instance().quit) #QCoreApplication.instance().quit is a slot of QT moduel internal,this signal also can connect a method which from user def.
        qbtn.clicked.connect(self.closeEvent)

        qbtn.resize(qbtn.sizeHint()) #sizeHint() return a default button size
        qbtn.move(175,50)

        self.setGeometry(300, 250, 300, 300)
        self.setWindowTitle('Tooltips and QuitButton')
        self.setWindowIcon(QIcon('pyqt5_demo3_pic.png')) #QIcon accept a pic path

        # class QDesktopWidget provide to us the inf of my pc desktop, like the screen resolution
        self.center() # the method which move the window to center

        self.show()

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

    def updateUi(self):
        self.browser.append("breakpoint")
        #time.sleep(20)
        try:
            text = unicode(self.lineedit.text())
            self.browser.append("%s = <b>%s</b>" % (text, eval(text)))
        except:
            self.browser.append(
                    "<font color=red>%s is invalid!</font>" % text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())