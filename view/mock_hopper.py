from pynput import keyboard
import time
import signal
import sys

class CoinHopper():
    def __init__(self, sensor_pin, relay_pin):
        self.start_time = time.time()
        self.sensor_pin = sensor_pin
        self.relay_pin = relay_pin
        self.empty = True

        listener = keyboard.Listener(on_press = self.on_press,
                                     on_release = self.on_release)
        listener.start()

    def drop_coin(self):
        print(self.empty)
        return self.empty

    def on_press(self, key):
        try:
            print('{0} pressed'.format(key.char))
        except AttributeError:
            print('{0} pressed'.format(key))

    def on_release(self, key):
        print('{0} pressed'.format(key))

        if key == keyboard.Key.esc:
            self.empty = False
        elif key == keyboard.Key.space:
            self.empty = True
