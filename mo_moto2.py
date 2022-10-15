# import time
import RPi.GPIO as GPIO
from time import sleep
M1PHASE=26
M1ENABLE=19

M2PHASE=6
M2ENABLE=13


# GPIO.setwarnings(False)

# mode = 4

GPIO.cleanup()

GPIO.setmode(GPIO.BCM)

GPIO.setup(M1ENABLE, GPIO.OUT)
GPIO.setup(M1PHASE, GPIO.OUT)

GPIO.setup(M2ENABLE, GPIO.OUT)
GPIO.setup(M2PHASE, GPIO.OUT)
# 
# GPIO.setup(mode, GPIO.OUT)
# GPIO.output(mode, GPIO.HIGH)

pwmA = GPIO.PWM(M1ENABLE, 1000)
pwmB = GPIO.PWM(M2ENABLE, 1000)

def forward():
    GPIO.output(M1PHASE, GPIO.LOW)
    GPIO.output(M2PHASE, GPIO.LOW)
    pwmA.start(20)
    pwmB.start(20)
    sleep(3)
    pwmA.ChangeDutyCycle(0)
    pwmB.ChangeDutyCycle(0)
    sleep(3)
    
    
def backward():

    GPIO.output(M1PHASE, GPIO.HIGH)
    GPIO.output(M2PHASE, GPIO.HIGH)
    pwmA.start(20)
    pwmB.start(20)
    sleep(3)
    pwmA.ChangeDutyCycle(0)
    pwmB.ChangeDutyCycle(0)
    sleep(3)
    



while True:
    forward()
    backward()

GPIO.cleanup()