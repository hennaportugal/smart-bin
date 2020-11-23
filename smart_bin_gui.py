import tkinter as tk
import RPi.GPIO as GPIO
import time
import inspect

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

class ProximitySensor():
    def __init__(self, trig_pin, echo_pin):
        print('Proximity Sensor', trig_pin, echo_pin)
        GPIO.setup(trig_pin, GPIO.OUT)
        GPIO.setup(echo_pin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

    def read_distance(self):
        print('read_distance')

    def display_distance(self):
        print('display_distance')

    def on_bin_full(self):
        print('on_bin_full')

    def run(self):
        print('run')

def main():
    sensor1 = ProximitySensor(14, 15)
    sensor1.read_distance()
    sensor1.display_distance()
    sensor1.on_bin_full()
    sensor1.run()

if __name__ == '__main__':
    main()

