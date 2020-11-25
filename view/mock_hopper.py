import time
import signal
import sys

class CoinHopper():
    def __init__(self, sensor_pin, relay_pin):
        self.start_time = time.time()
        self.sensor_pin = sensor_pin
        self.relay_pin = relay_pin

    def drop_coin(self):
        if (time.time() - self.start_time) >= 60:
            # return False to signify that the coin hopper is empty
            return False
        else:
            # return True to signify that coin has dropped
            return True
