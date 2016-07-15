import pygame.joystick
import threading
import serial
import sys
from PyQt5.QtWidgets import QMessageBox, QWidget, QProgressBar, QPushButton, QApplication, QGridLayout
from time import sleep

__author__ = 'Ninfeion'

DataCollectFlag = True

class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.updateUI()

    def updateUI(self):
        self.a1bar = QProgressBar(self) # create a progressbar that default range cover 0~99
        self.a1bar.setGeometry(30, 40, 200, 25)
        self.a1bar.setMaximum(1999)

        self.a2bar = QProgressBar(self)
        self.a2bar.setGeometry(30, 80, 200, 25)
        self.a2bar.setMaximum(1999)

        self.a3bar = QProgressBar(self)
        self.a3bar.setGeometry(30, 120, 200, 25)
        self.a3bar.setMaximum(1999)

        self.a4bar = QProgressBar(self)
        self.a4bar.setGeometry(30, 160, 200, 25)
        self.a4bar.setMaximum(1999)

        self.a5bar = QProgressBar(self)
        self.a5bar.setGeometry(30, 200, 200, 25)
        self.a5bar.setMaximum(1999)

        self.setGeometry(300, 300, 280, 280)
        self.setWindowTitle('BBflight Client')
        self.show()

    def closeEvent(self, QCloseEvent):
        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)  # Quit question messagebox set

        if reply == QMessageBox.Yes:
            QCloseEvent.accept()
            global DataCollectFlag
            DataCollectFlag = False
        else:
            QCloseEvent.ignore()

class devController(object):
    def __init__(self, JoystickNum):
        self._instancejoystick = pygame.joystick.Joystick(JoystickNum)
        self._instancejoystick.init()

        self.name = self._instancejoystick.get_name()
        self.id = self._instancejoystick.get_id()
        self.axesNum = self._instancejoystick.get_numaxes()
        self.ballsNum = self._instancejoystick.get_numballs()
        self.buttonsNum = self._instancejoystick.get_numbuttons()
        self.hatsNum = self._instancejoystick.get_numhats()

    def _eventRefresh(self):
        pygame.event.get()

    def getControllerData(self):
        self._axis = []
        self._ball = []
        self._hat = []
        self._button = []

        self._eventRefresh()
        for i in range(self.axesNum):
            self._axis.append(float("%1.3f" % self._instancejoystick.get_axis(i)))
            #print("Axis %i value: %f \n" % (i, self._axis[-1]))
        for i in range(self.buttonsNum):
            self._button.append(self._instancejoystick.get_button(i))
            #print("Button %i value: %s \n" % (i, self._button[-1]))
        for i in range(self.ballsNum):
            self._ball.append(self._instancejoystick.get_ball(i))
            #print("Ball %i value: %s \n" % (i, str(self._ball[-1])))
        for i in range(self.hatsNum):
            self._hat.append(self._instancejoystick.get_hat(i))
            #print("Hat %i value: %s \n" % (i, str(self._hat[-1])))

        return self._axis,self._button,self._hat,self._ball #return a tuple which including lists

#class devBearer(object):
#    def __init__(self):
#        pass

class dataQueue(object):
    def __init__(self):
        pass

def joystickModuelInit():
    pygame.init()
    pygame.joystick.init()
    return True

def joystickCheck():
    return pygame.joystick.get_count()

def uiDataRefresh(datatuple, tarobject):
    #datatuple = BBController.getControllerData()
    tarobject.a1bar.setValue(datatuple[0][0] * 1000 + 1000 + 1)
    tarobject.a2bar.setValue(datatuple[0][1] * 1000 + 1000 + 1)
    tarobject.a3bar.setValue(datatuple[0][2] * 1000 + 1000 + 1)
    tarobject.a4bar.setValue(datatuple[0][3] * 1000 + 1000 + 1)
    tarobject.a5bar.setValue(datatuple[0][4] * 1000 + 1000 + 1)

def main():

    app = QApplication(sys.argv)
    BBUI = MainWidget()

    print('BBflight Radio System Launch! \n')
    joystickModuelInit()
    #global joysticksNum
    joysticksNum = joystickCheck()
    BBController = devController(JoystickNum = joysticksNum - 1)

    threading_sys = threading.Thread(target = sys.exit, args = (sys.argv,))
    threading_sys.setDaemon(True)
    threading_sys.start()

    global DataCollectFlag
    while DataCollectFlag == True:
        dataOfController = BBController.getControllerData()
        uiDataRefresh(dataOfController, BBUI)

    serBearer = serial.Serial(port = "com3",
                              baudrate = 115200,  # baud rate
                              timeout = None)
    try:
        serBearer.write(b'HandShaking')
        sleep(0.05) #delay 50ms
    except EnvironmentError as err:
        print(err)
    finally:
        serBearer.close()


if __name__ == "__main__":
    main()

#clock = pygame.time.Clock()
#clock.tick(2) delay:frame/per sec
