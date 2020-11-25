import tkinter as tk
import RPi.GPIO as GPIO
import time
import inspect

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

class ProximitySensor():
    def __init__(self, trig_pin, echo_pin):
        self.trig_pin = trig_pin
        self.echo_pin = echo_pin

        self.empty_bin_distance = 20

        GPIO.setup(self.trig_pin, GPIO.OUT)
        GPIO.setup(self.echo_pin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
        GPIO.output(self.trig_pin, False)

    def __del__(self):
        # clean up GPIO state
        # GPIO clean()
        print('ProximitySensor::del')

    def read_distance(self):
        GPIO.output(self.trig_pin, True)
        time.sleep(0.00001)
        GPIO.output(self.trig_pin, False)

        pulse_start= time.time()
        pulse_end= time.time()

        while GPIO.input(self.echo_pin) == 0:
            pulse_start= time.time()
        while GPIO.input(self.echo_pin) == 1:
            pulse_end= time.time()
        pulse_duration = pulse_end - pulse_start

        distance = (pulse_duration * 34300) / 2

        if distance <= 500:
            return distance
        else:
            return None

    def is_bin_full(self):
        distance = self.read_distance()
        if distance == None:
            return False

        return (distance <= self.empty_bin_distance and distance > 0)
