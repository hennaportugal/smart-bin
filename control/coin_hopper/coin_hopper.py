from time import sleep
import signal
import sys
import RPi.GPIO as GPIO

# SENSOR_GPIO = 16
# RELAY_GPIO = 12

GPIO.setmode(GPIO.BOARD)

class CoinHopper():
    def __init__(self, sensor_pin, relay_pin):
        self.sensor_pin = sensor_pin
        self.relay_pin = relay_pin
        GPIO.setup(self.sensor_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.relay_pin, GPIO.OUT)

    def __del__(self):
        GPIO.cleanup()

    def drop_coin():
        GPIO.output(self.relay_gpio, GPIO.HIGH)
        sleep(0.05)

        GPIO.output(self.relay_gpio, GPIO.LOW)
        sleep(0.02)
        channel = GPIO.wait_for_edge(self.sensor_pin, GPIO.RISING, timeout=5000)

        if channel is None:
            # return False to signify that the coin hopper is empty
            return False
        else:
            GPIO.output(self.relay_gpio, GPIO.HIGH)
            sleep(0.02)
            # return True to signify that coin has dropped
            return True
