import time
import os
from motor_control import MotorControl 
from motion_capture import MotionCapture
from object_classifier.garbage_classifier import GarbageClassifier
from watchdog.events import FileSystemEventHandler

class SmartBin_Handler(FileSystemEventHandler):
    def __init__(self):
        self.garbage_classifier = GarbageClassifier()
        self.motor_control = MotorControl()
        self.motion_capture = MotionCapture()

    def on_created(self, event):
        time.sleep(0.5)
        image, _ = os.path.splitext(event.src_path)
        print ('image name: ' + image)
        detected_garbage = self.garbage_classifier.run(image + '.jpg')

        self.motor_control.move_bin(detected_garbage)
        print ("Done move")
        self.motion_capture.run()
