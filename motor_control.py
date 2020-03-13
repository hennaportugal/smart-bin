from time import sleep
from collections import defaultdict
# from PIL import Image

class MotorControl:
    def __init__(self):
        # dictionary for motor movement
        self.bin_movement_dictionary = {
            'plasticBottle': self.move_to_pb_bin,
            'aluminumCan': self.move_to_ac_bin,
            'paperCup': self.move_to_pc_bin
        }
        #by default, move to unclassified bin, if detected object is in the dictionary, call the appropriate function
        self.bin_movements = defaultdict(lambda: self.move_to_unclassified, self.bin_movement_dictionary)

    def move_to_home(self):
        # movement of the motors here
        print('turned back to home')

    def move_to_pb_bin(self):
        # movement of the motors here
        print('turned motor to plastic bottle bin')
        sleep(1)
        self.move_to_home()

    def move_to_ac_bin(self):
        # movement of the motors here
        print('turned motor to aluminum can bin')
        sleep(1)
        self.move_to_home()

    def move_to_pc_bin(self):
        # movement of the motors here
        print('turned motor to paper cup bin')
        sleep(1)
        self.move_to_home()

    def move_to_unclassified(self):
        #movement of the motors here
        print('turned to unclassified bin')
        sleep(1)
        self.move_to_home()

    # function to control the motor based on the detected object, default movement calls the unclassified function
    def move_bin(self, detected_object):
        return self.bin_movements[detected_object]()