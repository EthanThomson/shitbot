#Import Library
import Rpi.GPIO as GPIO
import time
#Define pins
Motor1En = 16
Motor1A = 18
Motor1B = 22
#Setup pins
def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Motor1A,GPIO.OUT)
    GPIO.setup(Motor1B,GPIO.OUT)
    GPIO.setup(Motor1En,GPIO.OUT)
    pwm=GPIO.PWM(Motor1En,1000)
    pwm.start(0)
#Simple FSM
def loop():
#Stop 10s
    GPIO.output(Motor1En, GPIO.LOW)
    pwm.stop()
    time.sleep(10)
#Forward 5s
    pwm.start(0)
    pwm.ChangeDutyCycle(50)
    GPIO.output(Motor1En, GPIO.HIGH)
    GPIO.output(Motor1A, GPIO.HIGH)
    GPIO.output(Motor1B, GPIO.LOW)
    time.sleep(5)
#Stop 10s
    GPIO.output(Motor1En, GPIO.LOW)
    pwm.stop()
    time.sleep(10)
#Reverse 5s
    pwm.start(0)
    pwm.ChangeDutyCycle(100)
    GPIO.output(Motor1En, GPIO.HIGH)
    GPIO.output(Motor1A, GPIO.LOW)
    GPIO.output(Motor1B, GPIO.HIGH)
    time.sleep(5)
def destroy():
    GPIO.cleanup()
#Program starts from here
 If __name == ‘__main__’:
setup()
try:
    loop()
except KeyboardInterrupt:
    destroy()