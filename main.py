from motor_control import MotorControl 
from object_classifier.garbage_classifier import GarbageClassifier

# This function will trigger the camera to capture the image when an item is placed on the orifice. This will then store the image somewhere for usage.
def mocap():
    # Dummy code
    object_detected = input('Did you capture anything?')
    if object_detected == 'yes':
        return True
    elif object_detected == 'no':
        return False

def main():
    motor_control = MotorControl()
    garbage_classifier = GarbageClassifier()

    while(1):
        # skip the rest of the code if motion capture has not detected an item
        if (not mocap()):
            continue

        detected_garbage = garbage_classifier.run()

        if detected_garbage:
            motor_control.move_bin(detected_garbage)
        else:
            motor_control.move_to_unclassified()

if __name__ == "__main__":
    main()
