from time import sleep
from collections import defaultdict
import RPi.GPIO as GPIO
import sys, tty, termios
# ~ from PIL import Image

#GPIO pins

GPIO.setmode(GPIO.BCM)
DIR = 20
STEP = 21
MODE = (18, 23, 24)
PUSH = 17     #Push linear actuator
PULL = 27     #Pull linear actuator

#GPIO values
CW = 1
CCW = 0
SPR = 200
RESOLUTION = (1, 0, 1) #1/32
delay = 0.0208/72

#GPIO motor init
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(MODE, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.setwarnings(False)

#LAC init
GPIO.setup(PULL, GPIO.OUT)
GPIO.setup(PUSH, GPIO.OUT)


class MotorControl:
    def __del__(self):
        GPIO.cleanup()

    def move_lac(self):
        #movement of linear actuator to push detected object after motor turns
        print ('LAC')
        print ('PUSH')
        sleep(1)
        GPIO.output(PUSH, GPIO.LOW)
        GPIO.output(PULL, GPIO.HIGH)
        sleep(3)
        GPIO.output(PUSH, GPIO.HIGH)
        GPIO.output(PULL, GPIO.HIGH)
        print ('PULL')
        sleep(1)
        GPIO.output(PUSH, GPIO.HIGH)
        GPIO.output(PULL, GPIO.LOW)
        sleep(4)
        GPIO.output(PUSH, GPIO.HIGH)
        GPIO.output(PULL, GPIO.HIGH)
        sleep(delay)

    def move_motor(self, direction, step_count):
        #move motors to specified direction and step count
        print ('MOTOR', direction, step_count)
        GPIO.output(DIR, direction)
        for _ in range(step_count):
            GPIO.output(STEP, GPIO.HIGH)
            sleep(delay)
            GPIO.output(STEP, GPIO.LOW)
            sleep(delay)

        self.move_lac()
        self.move_home(not direction, step_count)

    def move_home(self, direction, step_count):
        #move angle here reverse
        sleep(1)
        GPIO.output(DIR, direction)
        for _ in range(step_count):
            GPIO.output(STEP, GPIO.HIGH)
            sleep(delay)
            GPIO.output(STEP, GPIO.LOW)
            sleep(delay)

    # function to control the motor based on the detected object, default movement calls the unclassified function
    def move_bin(self, detected_object):
        print('move_bin')
        if detected_object == 'plasticBottle':
            self.move_motor(CW, SPR*20)
        elif detected_object == 'aluminumCan':
            self.move_motor(CCW, SPR*5)
        elif detected_object ==  'paperCup':
            self.move_motor(CW, SPR*12)
        else:
            self.move_motor(CW, SPR*5)
