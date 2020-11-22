from time import sleep
import RPi.GPIO as GPIO
import sys,tty,termios

GPIO.setmode(GPIO.BCM)


#Stepper
DIR=20
STEP=21
CW=1
CCW=0
SPR=200
MODE=(18,23,24)
GPIO.setup(DIR, GPIO.OUT)
GPIO.output(DIR,CW)
GPIO.setup(MODE, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.setwarnings(False)
#LAC
PUSH=17  #Push linearact before 17
PULL=27     #Pull linearact

GPIO.setup(PULL, GPIO.OUT)
GPIO.setup(PUSH, GPIO.OUT)

RESOLUTION= {'FULL':(0,0,0),'HALF':(1,0,0),'1/4':(0,1,0),'1/8':(1,1,0),'1/16':(0,0,1),'1/32':(1,0,1)}
         #  [0,1,1,32],
         # [1,1,1,32]]
#GPIO.output(MODE,RESOLUTION['HALF'])
#step_count=SPR*2
#delay=0.0208/2

#GPIO.output(MODE,RESOLUTION['1/16'])
#step_count=SPR*1
#delay=0.0208/32


#GPIO.output(MODE,RESOLUTION['1/32'])
#step_count=SPR*32
#delay=0.0208/32


while True:
        #GPIO.output(MODE,RESOLUTION['1/4'])
        #step_count=SPR
        delay=0.0208/84
      
        k=raw_input('')
        print 'MODE:',k
        if k=='1':             
                GPIO.output(MODE,RESOLUTION['1/32'])                          
                print ('Unclassified')
                GPIO.output(DIR,CW)
                step_count=SPR*5
                for x in range(step_count):             
                        GPIO.output(STEP, GPIO.HIGH)
                        sleep(delay)
                        GPIO.output(STEP, GPIO.LOW)
                        sleep(delay) 
                print ('PUSH')
                sleep(1)
                GPIO.output(PUSH, GPIO.LOW)
                GPIO.output(PULL, GPIO.HIGH)
                sleep(3)
                GPIO.output(PUSH, GPIO.HIGH)
                GPIO.output(PULL, GPIO.HIGH)
                print ('PULL')
                sleep(1)
                GPIO.output(PUSH, GPIO.HIGH)
                GPIO.output(PULL, GPIO.LOW)
                sleep(4)
                GPIO.output(PUSH, GPIO.HIGH)
                GPIO.output(PULL, GPIO.HIGH)
                sleep(delay)
                sleep(1)
                step_count=0
                print ('Go to Home')
                GPIO.output(DIR,CCW)
                step_count=SPR*5
                for x in range(step_count):             
                        GPIO.output(STEP, GPIO.HIGH)
                        sleep(delay)
                        GPIO.output(STEP, GPIO.LOW)
                        sleep(delay)
     
        elif k=='2':                                    
                GPIO.output(MODE,RESOLUTION['1/32'])                          
                print ('Paper Cups')
                GPIO.output(DIR,CW)
                step_count=SPR*12
                for x in range(step_count):             
                        GPIO.output(STEP, GPIO.HIGH)
                        sleep(delay)
                        GPIO.output(STEP, GPIO.LOW)
                        sleep(delay)
                print ('PUSH')
                sleep(1)
                GPIO.output(PUSH, GPIO.LOW)
                GPIO.output(PULL, GPIO.HIGH)
                sleep(3)
                GPIO.output(PUSH, GPIO.HIGH)
                GPIO.output(PULL, GPIO.HIGH)
                print ('PULL')
                sleep(1)
                GPIO.output(PUSH, GPIO.HIGH)
                GPIO.output(PULL, GPIO.LOW)
                sleep(4)
                GPIO.output(PUSH, GPIO.HIGH)
                GPIO.output(PULL, GPIO.HIGH)
                sleep(delay)
                sleep(1)
                step_count=0
                print ('Go to Home')
                GPIO.output(DIR,CCW)
                step_count=SPR*12
                for x in range(step_count):             
                        GPIO.output(STEP, GPIO.HIGH)
                        sleep(delay)
                        GPIO.output(STEP, GPIO.LOW)
                        sleep(delay)
                        
        elif k=='3':       
                GPIO.output(MODE,RESOLUTION['1/32'])                          
                print ('Plastic Bottles')
                GPIO.output(DIR,CW)
                step_count=SPR*20
                for x in range(step_count):             
                        GPIO.output(STEP, GPIO.HIGH)
                        sleep(delay)
                        GPIO.output(STEP, GPIO.LOW)
                        sleep(delay)
                print ('PUSH')
                sleep(1)
                GPIO.output(PUSH, GPIO.LOW)
                GPIO.output(PULL, GPIO.HIGH)
                sleep(3)
                GPIO.output(PUSH, GPIO.HIGH)
                GPIO.output(PULL, GPIO.HIGH)
                print ('PULL')
                sleep(1)
                GPIO.output(PUSH, GPIO.HIGH)
                GPIO.output(PULL, GPIO.LOW)
                sleep(4)
                GPIO.output(PUSH, GPIO.HIGH)
                GPIO.output(PULL, GPIO.HIGH)
                sleep(delay)
                sleep(1)
                step_count=0
                print ('Go to Home')
                GPIO.output(DIR,CCW)
                step_count=SPR*20
                for x in range(step_count):             
                        GPIO.output(STEP, GPIO.HIGH)
                        sleep(delay)
                        GPIO.output(STEP, GPIO.LOW)
                        sleep(delay) 

        elif k=='4':       
                GPIO.output(MODE,RESOLUTION['1/32'])                          
                print ('Aluminum Cans')
                GPIO.output(DIR,CCW)
                step_count=SPR*5
                for x in range(step_count):             
                        GPIO.output(STEP, GPIO.HIGH)
                        sleep(delay)
                        GPIO.output(STEP, GPIO.LOW)
                        sleep(delay) 
                print ('PUSH')
                sleep(1)
                GPIO.output(PUSH, GPIO.LOW)
                GPIO.output(PULL, GPIO.HIGH)
                sleep(3)
                GPIO.output(PUSH, GPIO.HIGH)
                GPIO.output(PULL, GPIO.HIGH)
                print ('PULL')
                sleep(1)
                GPIO.output(PUSH, GPIO.HIGH)
                GPIO.output(PULL, GPIO.LOW)
                sleep(4)
                GPIO.output(PUSH, GPIO.HIGH)
                GPIO.output(PULL, GPIO.HIGH)
                sleep(delay)
                sleep(1)
                step_count=0
                print ('Go to Home')
                GPIO.output(DIR,CW)
                step_count=SPR*5
                for x in range(step_count):             
                        GPIO.output(STEP, GPIO.HIGH)
                        sleep(delay)
                        GPIO.output(STEP, GPIO.LOW)
                        sleep(delay)
        elif k=='5':       
                GPIO.output(MODE,RESOLUTION['1/32'])                          
                print ('Reset')
                GPIO.output(DIR,CW)
                step_count=SPR
                for x in range(step_count):             
                        GPIO.output(STEP, GPIO.HIGH)
                        sleep(delay)
                        GPIO.output(STEP, GPIO.LOW)
                        sleep(delay) 
                print ('PULL')
                sleep(1)
                GPIO.output(PUSH, GPIO.HIGH)
                GPIO.output(PULL, GPIO.LOW)
                sleep(4)
                GPIO.output(PUSH, GPIO.HIGH)
                GPIO.output(PULL, GPIO.HIGH)
        elif k=='6':       
                GPIO.output(MODE,RESOLUTION['1/32'])                          
                print ('Reset')
                GPIO.output(DIR,CCW)
                step_count=SPR
                for x in range(step_count):             
                        GPIO.output(STEP, GPIO.HIGH)
                        sleep(delay)
                        GPIO.output(STEP, GPIO.LOW)
                        sleep(delay) 
        
        else:
            print "INVALID"
            GPIO.cleanup()
            




