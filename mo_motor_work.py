# import time

# motors connection from left (pink, blue) Left motor ///(yellow, green) right motor
import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
import time
M1PHASE=15
M1ENABLE=14

M2PHASE=25
M2ENABLE=24

Mode=18




servoGrabFront = 23

#define right arm servo
RightservoPIN = 12

# left servo is not used, one servo is enough to lift everything
#LeftservoPIN = 13

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoGrabFront , GPIO.OUT)
GPIO.setup(RightservoPIN , GPIO.OUT)
#GPIO.setup(LeftservoPIN , GPIO.OUT)

servoGrab  = GPIO.PWM(servoGrabFront , 50)

Rightservo = GPIO.PWM(RightservoPIN , 50)
#Leftservo  = GPIO.PWM(LeftservoPIN , 50)
Rightservo.start(0)
#Leftservo.start(0)
servoGrab.start(0)




















# Do no delete thes lines
# M1PHASE=26
# M1ENABLE=19
# 
# M2PHASE=6
# M2ENABLE=13



GPIO.setmode(GPIO.BCM)
GPIO.setup(Mode, GPIO.OUT)
GPIO.output(Mode, GPIO.HIGH)

GPIO.setup(M1ENABLE, GPIO.OUT)
GPIO.setup(M1PHASE, GPIO.OUT)

GPIO.setup(M2ENABLE, GPIO.OUT)
GPIO.setup(M2PHASE, GPIO.OUT)
# 


pwmA = GPIO.PWM(M1ENABLE, 1000)
pwmB = GPIO.PWM(M2ENABLE, 1000)
pwmA.start(0)
pwmB.start(0)
def forward():
    print("Motor Forward")
    GPIO.output(M1PHASE, GPIO.LOW)
    GPIO.output(M2PHASE, GPIO.LOW)

    #sleep(2)
    pwmA.ChangeDutyCycle(3)
    pwmB.ChangeDutyCycle(3)
    sleep(2)
    
    
def backward():
    print("Motor Backword")
    GPIO.output(M1PHASE, GPIO.HIGH)
    GPIO.output(M2PHASE, GPIO.HIGH)

    sleep(2)
    pwmA.ChangeDutyCycle(3)
    pwmB.ChangeDutyCycle(3)
    sleep(2)
    
def RServoDown():
    duty=6
    print("Servo Down")
    while duty >=3.6:
        
        Rightservo.ChangeDutyCycle(duty)
        time.sleep(0.1)
        duty=duty-0.1
        
    Rightservo.ChangeDutyCycle(0)


def RServoUp():
    duty=5
    print("Servo Up")
    while duty <=7:
        
        Rightservo.ChangeDutyCycle(duty)
        time.sleep(0.1)
        duty=duty+0.1       
        
    Rightservo.ChangeDutyCycle(0)  

try:
    while True:
        #forward()
        #time.sleep(0.5)
        RServoDown()
        time.sleep(3)
        RServoUp()
        time.sleep(3)
        #backward()

    
finally:
    
    pwmA.ChangeDutyCycle(0)
    pwmB.ChangeDutyCycle(0)
    pwmA.stop()
    pwmB.stop()
    GPIO.cleanup()