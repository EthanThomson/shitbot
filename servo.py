import time
import RPi.GPIO as GPIO


# GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

# set GPIO Pins
rot = 19

GPIO.setup(rot, GPIO.IN)

pwmA = GPIO.PWM(rot, 50)


def forward():
    GPIO.output(rot, GPIO.LOW)
    pwmA.start(20)
    time.sleep(3)
    pwmA.ChangeDutyCycle(0)
    time.sleep(3)

while 1:
    forward()
