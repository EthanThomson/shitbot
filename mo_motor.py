import RPi.GPIO as gpio
import time

gpio.setwarnings(False)

bphase = 24
benable = 23
aphase = 2
aenable = 17
mode = 4

gpio.setmode(gpio.BCM)
gpio.setup(bphase, gpio.OUT)
gpio.setup(benable, gpio.OUT)
gpio.setup(aphase, gpio.OUT)
gpio.setup(aenable, gpio.OUT)
gpio.setup(mode, gpio.OUT)

while 1:
    pwmB = gpio.PWM(benable, 1000)
    pwmB.start(20)
    pwmA = gpio.PWM(aenable, 1000)
    pwmA.start(20)


    #Forward 5s
    # pwm.start(0)
    pwmA.ChangeDutyCycle(50)
    pwmB.ChangeDutyCycle(50)
    gpio.output(mode, gpio.HIGH)
    gpio.output(benable, gpio.HIGH)
    gpio.output(aenable, gpio.HIGH)
    gpio.output(bphase, gpio.LOW)
    gpio.output(aphase, gpio.LOW)
    time.sleep(2)


