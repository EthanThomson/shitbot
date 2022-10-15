import RPi.GPIO as GPIO
import time

# define duty to turn servo in steps

#define grabber servo
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



def RServoDown():
    duty=7
    print("Servo Down")
    while duty >=3.6:
        
        Rightservo.ChangeDutyCycle(duty)
        time.sleep(0.1)
        duty=duty-0.1
        
    Rightservo.ChangeDutyCycle(0)


def RServoMid():
    duty=4
    print("Servo Mid")
    while duty <=6:
        
        Rightservo.ChangeDutyCycle(duty)
        time.sleep(0.1)
        duty=duty+0.1
    Rightservo.ChangeDutyCycle(0)
    
def RServoUp():
    duty=6
    print("Servo Up")
    while duty <=7:
        
        Rightservo.ChangeDutyCycle(duty)
        time.sleep(0.1)
        duty=duty+0.1       
        
    Rightservo.ChangeDutyCycle(0)   




def grab():
    
    servoGrab.ChangeDutyCycle(7)
    
    time.sleep(0.5)
    servoGrab.ChangeDutyCycle(0)
    
    time.sleep(2)
    


def drop():
    
    servoGrab.ChangeDutyCycle(5)
    
    time.sleep(0.5)
    servoGrab.ChangeDutyCycle(0)
    time.sleep(2)





#Left Servo
    
# def LServoDown():
#     duty=8
#     print("Left Servo Down")
#     while duty <=17:
#         
#         Leftservo.ChangeDutyCycle(duty)
#         time.sleep(0.1)
#         duty=duty+0.1       
#         
#     Leftservo.ChangeDutyCycle(0)       
#     
# def LServoMid():
#     duty=17
#     print("Left Servo Mid")
#     while duty >=8:
#         
#         Leftservo.ChangeDutyCycle(duty)
#         time.sleep(0.1)
#         duty=duty-0.1       
#         
#     Leftservo.ChangeDutyCycle(0)  


######Right servo control
RServoDown()
time.sleep(2)

grab()
time.sleep(2)
#  
RServoMid()
time.sleep(2)
# 
drop()
time.sleep(2)
# # # 
RServoUp()
time.sleep(2)
# 
#Rightservo.stop()



# 
# LServoDown()
# time.sleep(1)
# 
# LServoMid()
# time.sleep(1)


GPIO.cleanup()
print("Servo Stop")
