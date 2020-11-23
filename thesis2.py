import tkinter as tk
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)

#setup for GPIO 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

binCapacity ="Empty"

TRIG1=14
ECHO1=15
TRIG2=23
ECHO2=24
TRIG3=25
ECHO3=8
TRIG4=7
ECHO4=1

GPIO.setup(TRIG1,GPIO.OUT)
GPIO.setup(TRIG2,GPIO.OUT)
GPIO.setup(TRIG3,GPIO.OUT)
GPIO.setup(TRIG4,GPIO.OUT)
GPIO.setup(ECHO1, GPIO.IN, pull_up_down= GPIO.PUD_DOWN)
GPIO.setup(ECHO2, GPIO.IN, pull_up_down= GPIO.PUD_DOWN)
GPIO.setup(ECHO3, GPIO.IN, pull_up_down= GPIO.PUD_DOWN)
GPIO.setup(ECHO4, GPIO.IN, pull_up_down= GPIO.PUD_DOWN)

root = tk.Tk()
root.title("SMARTBin 2")

#SECTION FOR READING SENSOR DISTANCE
def read_distance1(sensor1):
    GPIO.output(TRIG1, False)
    time.sleep(2)
    GPIO.output(TRIG1, True)
    time.sleep(0.00001)
    GPIO.output(TRIG1, False)
    while GPIO.input(ECHO1)==0:
        pulse_start= 0
    pulse_start= time.time()
    while GPIO.input(ECHO1)==1:
        pulse_end= 0
    pulse_end= time.time()
    pulse_duration = pulse_end-pulse_start
    distance1= pulse_duration*18000
    distance1= round(distance1,2)
    sensor1.set(str(distance1) + ' cm')
    print('ALUMINUM CANS:',distance1,'cm')
    # clean up GPIO state
    # GPIO clean()
    #distance over 500 is considered noise
    #1
    if distance1 <= 500:
        time.sleep(2)
        return distance1
    else:
        time.sleep(2)
        return None


def read_distance2():

    GPIO.output(TRIG2, False)
    time.sleep(2)
    GPIO.output(TRIG2, True)
    time.sleep(0.00001)
    GPIO.output(TRIG2, False)
    while GPIO.input(ECHO2)==0:
        pulse_start= 0
    pulse_start= time.time()
    while GPIO.input(ECHO2)==1:
        pulse_end= 0
    pulse_end= time.time()
    pulse_duration = pulse_end-pulse_start
    distance2= pulse_duration*18000
    distance2= round(distance2,2)
    sensor2.set(str(distance2)+' cm')
    print('PAPER CUPS:',distance2,'cm')
    
    # clean up GPIO state
    # GPIO clean()
    #distance over 500 is considered noise
    #1
    if distance2 <= 500:
            time.sleep(2)
            return distance2
    else: 
            time.sleep(2)
            return None

def read_distance3():
    GPIO.output(TRIG3, False)
    time.sleep(2)
    GPIO.output(TRIG3, True)
    time.sleep(0.00001)
    GPIO.output(TRIG3, False)
    while GPIO.input(ECHO3)==0:
        pulse_start= 0
    pulse_start= time.time()
    while GPIO.input(ECHO3)==1:
        pulse_end= 0
    pulse_end= time.time()
    pulse_duration = pulse_end-pulse_start
    distance3= pulse_duration*18000
    distance3= round(distance3,2)
    sensor3.set(str(distance3)+' cm')
    print('PLASTIC BOTTLES:',distance3,'cm')
    
    # clean up GPIO state
    # GPIO clean()
    #distance over 500 is considered noise
    #1
    if distance3 <= 500:
            time.sleep(2)
            return distance3
    else: 
            time.sleep(2)
            return None

def read_distance4():
    GPIO.output(TRIG4, False)
    time.sleep(2)
    GPIO.output(TRIG4, True)
    time.sleep(0.00001)
    GPIO.output(TRIG4, False)
    while GPIO.input(ECHO4)==0:
        pulse_start= 0
    pulse_start= time.time()
    while GPIO.input(ECHO4)==1:
        pulse_end= 0
    pulse_end= time.time()
    pulse_duration = pulse_end-pulse_start
    distance4= pulse_duration*18000
    distance4= round(distance4,2)
    sensor4.set(str(distance4)+' cm')
    print('PAPER CUPS:',distance4,'cm')
    
    # clean up GPIO state
    # GPIO clean()
    #distance over 500 is considered noise
    #1
    if distance4 <= 500:
            time.sleep(2)
            return distance4
    else: 
            time.sleep(2)
            return None

if __name__ == '__main__':
    while True:
        start_time = time.time()
        distance1 = read_distance1()    #for sensor 1
        distance2 = read_distance2()    #for sensor 2     
        distance3 = read_distance3()    #for sensor 3    
        distance4 = read_distance4()    #for sensor 4
    #1
    if distance1:
        label = tk.Label(root,textVariable=sensor1,width=40, fg="yellow" , bg = "green")
        label.config(font=("Courier", 36))
        label.config(text=str(distance1))
        label.pack()
    
        GPIO.output(TRIG1, False)
        print ("Delay for sensor stability")
        time.sleep(2)
        GPIO.output(TRIG1, True)
        time.sleep(0.00001)
        GPIO.output(TRIG1, False)
        print ("Distance:",distance1,"cm")

        if distance1 <= 20 and distance1 > 0:
            if binCapacity == "Empty":
                binCapacity = "Full"
                label = tk.Label(root,textVariable=sensor1,width=40, fg="yellow" , bg = "red")
            else:
                label = tk.Label(root,textVariable=sensor1,width=40, fg="yellow" , bg = "red")
    elif distance1 > 20:
        if binCapacity == "FULL":
            binCapacity = "Empty"
            label = tk.Label(root,textVariable=sensor1,width=40, fg="yellow" , bg = "green")
        else:
            label = tk.Label(root,textVariable=sensor1,width=40, fg="yellow" , bg = "green")
    else:
        wait = start_time + 1 - time.time()
    if wait > 0:
        time.sleep(wait)
    
    #2
    if distance2:
        label = tk.Label(root,textVariable=sensor2,width=40, fg="yellow" , bg = "green")
        label.config(font=("Courier", 36))
        label.config(text=str(distance2))
        label.pack()

        GPIO.output(TRIG2, False)
        print ("Delay for sensor stability")
        time.sleep(2)
        GPIO.output(TRIG2, True)
        time.sleep(0.00001)
        GPIO.output(TRIG2, False)
        print ("Distance:",distance2,"cm")

        if distance2 <= 20 and distance2 > 0:
            if binCapacity == "Empty":
                binCapacity = "Full"
                label = tk.Label(root,textVariable=sensor2,width=40, fg="yellow" , bg = "red")    
        else:
            label = tk.Label(root,textVariable=sensor2,width=40, fg="yellow" , bg = "red")
    elif distance2 > 20:
        if binCapacity == "FULL":
            binCapacity = "Empty"
            label = tk.Label(root,textVariable=sensor2,width=40, fg="yellow" , bg = "red")
        else:
            label = tk.Label(root,textVariable=sensor2,width=40, fg="yellow" , bg = "red")
    else:
        wait = start_time + 1 - time.time()
    if wait > 0:
        time.sleep(wait)
   
    #3
    if distance3:
        label = tk.Label(root,textVariable=sensor3,width=40, fg="yellow" , bg = "green")
        label.config(font=("Courier", 36))
        label.config(text=str(distance3))
        label.pack()

        GPIO.output(TRIG3, False)
        print ("Delay for sensor stability")
        time.sleep(2)
        GPIO.output(TRIG3, True)
        time.sleep(0.00001)
        GPIO.output(TRIG3, False)
        print ("Distance:",distance3,"cm")

        if distance3 <= 20 and distance3 > 0:
            if binCapacity == "Empty":
                binCapacity = "Full"
                label = tk.Label(root,textVariable=sensor3,width=40, fg="yellow" , bg = "red")    
        else:
            label = tk.Label(root,textVariable=sensor3,width=40, fg="yellow" , bg = "red")
    elif distance3 > 20:
        if binCapacity == "FULL":
            binCapacity = "Empty"
            label = tk.Label(root,textVariable=sensor3,width=40, fg="yellow" , bg = "green")
        else:
            label = tk.Label(root,textVariable=sensor3,width=40, fg="yellow" , bg = "green")
    else:
        wait = start_time + 1 - time.time()
    if wait > 0:
        time.sleep(wait)

    #4
    if distance4:
        label = tk.Label(root,textVariable=sensor4,width=40, fg="yellow" , bg = "green")
        label.config(font=("Courier", 36))
        label.config(text=str(distance4))
        label.pack()

        GPIO.output(TRIG4, False)
        print ("Delay for sensor stability")
        time.sleep(2)
        GPIO.output(TRIG4, True)
        time.sleep(0.00001)
        GPIO.output(TRIG4, False)
        print ("Distance:",distance4,"cm")

        if distance4 <= 20 and distance4 > 0:
            if binCapacity == "Empty":
                binCapacity = "Full"
                label = tk.Label(root,textVariable=sensor4,width=40, fg="yellow" , bg = "red")    
        else:
            label = tk.Label(root,textVariable=sensor4,width=40, fg="yellow" , bg = "red")    
    elif distance4 > 20:
        if binCapacity == "FULL":
            binCapacity = "Empty"
            label = tk.Label(root,textVariable=sensor4,width=40, fg="yellow" , bg = "green")    
        else:
            label = tk.Label(root,textVariable=sensor4,width=40, fg="yellow" , bg = "green")    
    else:
        wait = start_time + 1 - time.time()
    if wait > 0:
        time.sleep(wait)


    root.mainloop()
    GPIO.cleanup()
