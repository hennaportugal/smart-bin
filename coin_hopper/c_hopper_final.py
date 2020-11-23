from time import sleep
import signal
import sys
import RPi.GPIO as GPIO

SENSOR_GPIO = 16
RELAY_GPIO = 12

GPIO.setmode(GPIO.BOARD)
GPIO.setup(SENSOR_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(RELAY_GPIO, GPIO.OUT)

def signal_handler(sig, frame):
    GPIO.cleanup()
    sys.exit(0)

def main():
    """
    ang goal sa code kay before maka user input kay di mu on ang relay, inig enter sa user input,
    diha mu on nya ig sense niya sa naay muagi nga coin nga rising edge, mustop ang relay and huwat,
    and loop again
    """

    while True:
        GPIO.output(RELAY_GPIO, GPIO.HIGH)
        user_input = int(input("put user input: "))
      
        if user_input >=1 and user_input <=4:
            GPIO.output(RELAY_GPIO, GPIO.LOW)
            sleep(0.02)
            channel = GPIO.wait_for_edge(SENSOR_GPIO, GPIO.RISING, timeout=5000)
        
            if channel is None:
                print "dispense timeout"
            else:
                GPIO.output(RELAY_GPIO, GPIO.HIGH)
                sleep(0.02)
        # ~ print "invalid input"
    signal.signal(signal.SIGINT, signal_handler)
    signal.pause()

if __name__ == '__main__':
    main()
