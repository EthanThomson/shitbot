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


pwmB = gpio.PWM(benable, 1000)
pwmB.start(0)
pwmA = gpio.PWM(aenable, 1000)
pwmA.start(0)

    #Forward 5s
# pwm.start(0)
pwmA.ChangeDutyCycle(50)
pwmB.ChangeDutyCycle(50)
gpio.output(mode, gpio.HIGH)
gpio.output(benable, gpio.HIGH)
gpio.output(aenable, gpio.HIGH)
gpio.output(bphase, gpio.LOW)
gpio.output(aphase, gpio.LOW)
time.sleep(1800)


    #Forward 5s
 #   pwma.start(0)
  #  pwmb.start(0)
   # pwm.ChangeDutyCycle(50)
   # gpio.output(a1, gpio.HIGH)
   # gpio.output(a2, gpio.LOW)
 #   gpio.output(b1, gpio.HIGH)
  #  gpio.output(b2, gpio.LOW)
   # time.sleep(5)
