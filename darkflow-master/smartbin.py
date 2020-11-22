# ~ from motor_control import MotorControl 
from motion_capture import MotionCapture 

# This function will trigger the camera to capture the image when an item is placed on the orifice. This will then store the image somewhere for usage.
def mocap():
    # Dummy code
    object_detected = input('Did you capture anything? ')
    if object_detected == 'yes':
        image_name = input('input image name: ')
        return True, image_name
    elif object_detected == 'no':
        return False, None

def main():
    # ~ motor_control = MotorControl()
    image_path = '/home/pi/darkflow-master/test_data/'
    motion_capture = MotionCapture()

    while(1):
        # skip the rest of the code if motion capture has not detected an item
        object_detected, image_name = mocap()
        if (not object_detected):
            continue

        motion_capture.run()
#        detected_garbage = garbage_classifier.run(image_path + image_name)

#        if detected_garbage:
            # ~ motor_control.move_bin(detected_garbage)
#            print("move")
#        else:
            # ~ motor_control.move_to_unclassified()
#            pass

if __name__ == '__main__':
    main()
