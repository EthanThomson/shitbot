
import RPi.GPIO as GPIO
import time

servoPIN1 = 23

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN1, GPIO.OUT)

# duty cycle needs to be 3 < x < 8
# 3.5 for arm servo to hold lego

servo1 = GPIO.PWM(servoPIN1, 50) # GPIO 19 for PWM with 50Hz

servo1.start(2.5) # Initialization

try:
  while True:
    servo1.ChangeDutyCycle(7)
    
    time.sleep(0.5)
    servo1.ChangeDutyCycle(0)
    
    time.sleep(2)
    
    servo1.ChangeDutyCycle(5)
    
    time.sleep(0.5)
    servo1.ChangeDutyCycle(0)
    time.sleep(2)

    

except KeyboardInterrupt:
  servo1.stop()
  GPIO.cleanup()
  

