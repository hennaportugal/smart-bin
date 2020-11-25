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

        GPIO.setup(self.trig_pin, GPIO.OUT)
        GPIO.setup(self.echo_pin, GPIO.IN)

    def __del__(self):
        # clean up GPIO state
        GPIO.cleanup()

    def read_distance(self):
        GPIO.output(self.trig_pin, False)
        time.sleep(2)
        GPIO.output(self.trig_pin, True)
        time.sleep(0.00001)
        GPIO.output(self.trig_pin, False)

        while GPIO.input(self.echo_pin) == 0:
            pulse_start = time.time()
            print("echo 0", self.trig_pin, self.echo_pin)

        while GPIO.input(self.echo_pin) == 1:
            pulse_end = time.time()
            print("echo 1", self.trig_pin, self.echo_pin)

        pulse_duration = (pulse_end - pulse_start)
        distance = round((pulse_duration * 17150), 2)

        print('ProximitySensor::distance', distance, self.trig_pin, self.echo_pin)

        if distance <= 500:
            return distance

    def is_bin_full(self):
        start_time = time.time()
        distance = self.read_distance()

        if distance <= 20 and distance > 0:
            return True
        elif distance > 20:
            return False
        else:
            wait = start_time + 1 - time.time()

        if wait > 0:
            time.sleep(wait)

        return False
