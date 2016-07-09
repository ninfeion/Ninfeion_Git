import pygame.joystick
import threading
import serial
from time import sleep

__author__ = 'Ninfeion'

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
        for i in self.axesNum:
            self._axis.append(self._instancejoystick.get_axis(i))
            print("Axis %i value: %f \n" % (i, self._axis[-1]))
        for i in self.buttonsNum:
            self._button.append(self._instancejoystick.get_button(i))
            print("Button %i value: %s \n" % (i, self._button[-1]))
        for i in self.ballsNum:
            self._ball.append(self._instancejoystick.get_ball(i))
            print("Ball %i value: %s \n" % (i, str(self._ball[-1])))
        for i in self.hatsNum:
            self._hat.append(self._instancejoystick.get_hat(i))
            print("Hat %i value: %s \n" % (i, str(self._hat[-1])))

        return self._axis,self._button,self._ball,self._hat #return a tuple which including lists

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

def main():
    print('BBflight Radio System Launch! \n')
    joystickModuelInit()
    #global joysticksNum
    joysticksNum = joystickCheck()
    print(joysticksNum)
    BBController = devController(JoystickNum = joysticksNum - 1)

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

    dataOfController = BBController.getControllerData()
    for i in BBController.axesNum:
        print("axis %i value: %f" %(i, dataOfController[0][i]))

if __name__ == "__main__":
    main()

#clock = pygame.time.Clock()
#clock.tick(2) delay:frame/per sec
