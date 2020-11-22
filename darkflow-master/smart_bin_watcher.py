import time
import cv2
from watchdog.observers import Observer
from smart_bin_handler import SmartBin_Handler
from motion_capture import MotionCapture

class SmartBin_Watcher:
    path = "/home/pi/darkflow-master/test_data" # final path is folder in Raspi 4 where motion project puts jpg images 
    
    def __init__(self):
        self.observer = Observer()
        self.smart_bin_handler = SmartBin_Handler()
        self.motion_capture = MotionCapture()
    
    def run(self):
        print ("smart_bin_watcher::run")
        self.observer.schedule(self.smart_bin_handler, self.path, recursive = True)
        self.observer.start()
        self.motion_capture.run()
        try:
            time.sleep(0.5)
        except:
            self.observer.stop()
        self.observer.join()

if __name__ == "__main__":
    main = SmartBin_Watcher()
    main.run()
