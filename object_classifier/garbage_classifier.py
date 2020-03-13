from darkflow.net.build import TFNet
import cv2
from subprocess import call

class GarbageClassifier():
    # init block ---> put every intialization here, camera, motors, sensors
    def __init__(self):
        #load darkflow model
        options = {"model": "C:/Development//repos/smart-bin/object_classifier/cfg/yolo.cfg", "load": "C:/Development//repos/smart-bin/object_classifier/bin/yolov2.weights", "threshold": 0.5, "gpu": 0.7}
        self.tfnet = TFNet(options)

    # returns the object you specify
    def get_target(self, classifiedObjects, target):
       for object in classifiedObjects:
           if object.get('label') == target:
               return object

    # function that returns the first object detected among all others returned by darkflow
    def get_first_object(self, classified_objects):
        print('classified object:', classified_objects[0].get('label'))
        return classified_objects[0].get('label')

    def run(self):
        img_captured = cv2.imread("C:/Development//repos/smart-bin/object_classifier/sample_img/sample_computer.jpg") # read the image that has been captured by the camera, which was triggered by mocap()

        # here you can check if there are classified objects
        result = self.tfnet.return_predict(img_captured)
        print("All the classified objects")
        print(result)

        return self.get_first_object(result)
