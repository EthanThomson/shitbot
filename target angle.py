from dis import dis
import math
import cv2
# import time

# motors connection from left (pink, blue) Left motor ///(yellow, green) right motor
import RPi.GPIO as GPIO
from time import sleep
import time
GPIO.setwarnings(False)
#Define motor 1
M1PHASE=15
M1ENABLE=14
#Define motor 2
M2PHASE=25
M2ENABLE=24

Mode=18
motor_dirrection= True

#define line followers

#Left line follower
line_follower_1_pin = 6
#RIght line follower
line_follower_2_pin = 5




GPIO.setmode(GPIO.BCM)
GPIO.setup(Mode, GPIO.OUT)
GPIO.output(Mode, GPIO.HIGH)

GPIO.setup(M1ENABLE, GPIO.OUT)
GPIO.setup(M1PHASE, GPIO.OUT)

GPIO.setup(M2ENABLE, GPIO.OUT)
GPIO.setup(M2PHASE, GPIO.OUT)
# line followers
GPIO.setup(line_follower_1_pin, GPIO.IN)
GPIO.setup(line_follower_2_pin, GPIO.IN)


pwmA = GPIO.PWM(M1ENABLE, 1000) # Left Motor
pwmB = GPIO.PWM(M2ENABLE, 1000) # Right Motor

pwmA.start(0)
pwmB.start(0)

GPIO.output(M1PHASE, GPIO.LOW)
GPIO.output(M2PHASE, GPIO.LOW)
def LineFollower():
    #set time
    global LeftSensor
    global RightSensor
    global motor_dirrection
#     T1 = time.time()
    
    LeftSensor=GPIO.input(line_follower_1_pin)
    RightSensor=GPIO.input(line_follower_2_pin)
    
#     print("Left Sensor: " + str(LeftSensor) + "  Right Sensor: " + str(RightSensor))
#     sleep(0.5)
#     T2 = time.time()
#     print(T2-T1)

    #setting the motor dirrection

    if LeftSensor == False and RightSensor == False :
        print("Go forward")
        motor_dirrection = "Go forward"
    elif LeftSensor == False and RightSensor == True :
        print("Turn Right")
        motor_dirrection = "Turn Right"
    elif LeftSensor == True and RightSensor == False :
        print("Turn Left")
        motor_dirrection = "Turn Left"
    else :
        print("Stop") # Both lines True
        motor_dirrection = "Stop"

    return motor_dirrection, LeftSensor, RightSensor
    
    
    

def MotorDirection():
    print("Motor Direction")
    
    if motor_dirrection == "Go forward":
        forward()

  
    elif motor_dirrection == "Turn Left":
        turnLeft()
        
    elif motor_dirrection == "Turn Right":
        turnRight()     
        
    else:
        motor_dirrection == "Stop"
        stop()
        
        
def stop():
    print("Motor Stop")
#     GPIO.output(M1PHASE, GPIO.LOW)
#     GPIO.output(M2PHASE, GPIO.LOW)

    #sleep(1)
    pwmA.ChangeDutyCycle(0)
    pwmB.ChangeDutyCycle(0)
    sleep(1)
    
def turnRight():
    
#     GPIO.output(M1PHASE, GPIO.LOW)
#     GPIO.output(M2PHASE, GPIO.LOW)

    #sleep(0.5) 
    pwmA.ChangeDutyCycle(0.5)
    pwmB.ChangeDutyCycle(0.05)
    sleep(0.5) 
def turnLeft():
    
#     GPIO.output(M1PHASE, GPIO.LOW)
#     GPIO.output(M2PHASE, GPIO.LOW)

    #sleep(1)
    pwmA.ChangeDutyCycle(0.01)
    pwmB.ChangeDutyCycle(0.5)    
    sleep(0.5) 
def forward():
    print("Motor Forward")
#     GPIO.output(M1PHASE, GPIO.LOW)
#     GPIO.output(M2PHASE, GPIO.LOW)

    #sleep(0.5) 
    pwmA.ChangeDutyCycle(9)
    pwmB.ChangeDutyCycle(10)
    sleep(0.5)    

    
def backward():
    print("Motor Backword")
    GPIO.output(M1PHASE, GPIO.HIGH)
    GPIO.output(M2PHASE, GPIO.HIGH)

    #sleep(3)
    pwmA.ChangeDutyCycle(9)
    pwmB.ChangeDutyCycle(10)
    sleep(0.5)
    
def rotate():
    print("Motor Rotate UntiClockWise") # Left motor backward, Right motor Forward
    GPIO.output(M1PHASE, GPIO.HIGH) # Left
    GPIO.output(M2PHASE, GPIO.LOW) # Right

    #sleep(3)
    pwmA.ChangeDutyCycle(10)
    pwmB.ChangeDutyCycle(10)
    sleep(0.5)   


def deg45():
    
    print("45 Degree ClockWise")
    GPIO.output(M1PHASE, GPIO.LOW)
    GPIO.output(M2PHASE, GPIO.HIGH)

    #sleep(3)
    pwmA.ChangeDutyCycle(10)
    pwmB.ChangeDutyCycle(10)
    sleep(0.5)

#Axle1, Axle2 = 4, 6
Axel=[4,6] # robot tail
#Nose_x1,Nose_y1= 3,5
Nose=[3,5] # nose of the robot

#target1, target2= 8,9
#target=[8,9] 

distance_list=[]
targets=([120,100],[82,55],[30,20],[4,20])#Bricks Coordinates
minDistance=0

def closestBrick():
    
    for near in targets:
  
        distance= math.dist(near,Axel)
        distance_list.append(distance)
        
    #minDistance=min(distance_list)
    index_min = min(range(len(distance_list)), key=distance_list.__getitem__)

    nearBrick=targets[index_min]
    print("Nearest Brick is :", nearBrick)
    
     
def getAngle():
    global error_angle
    global CWerror_angle
    global CCWerror_angle
    
    
        
    
    
    angle= math.atan2(Nose[0]-Axel[0], Nose[1]-Axel[1])

    mydegrees = math.degrees(angle)
    print(mydegrees)

    targetPoint= math.atan2(target1-Nose_x1, target2-Axle2) # i nead to get the coordinate of the closest brick
    
    targetPoint = math.degrees(targetPoint)
    print(targetPoint)
    
    error_angle=targetPoint-mydegrees
    print("CWError",error_angle)
    print("CCWerror",error_angle-360)
    CWerror_angle=abs(error_angle)
    CCWerror_angle=abs(error_angle-360)
    
    print(abs(error_angle))
    print(abs(error_angle-360))
   
def rotation():
    
    if CCWerror_angle < CWerror_angle:
        print("Rotate CCW")
        CCW_motor()
        
    else:
        print("Rotate CW")
        CW_motor()
             
def CCW_motor():
        
        GPIO.output(M1PHASE, GPIO.HIGH)
        GPIO.output(M2PHASE, GPIO.LOW)

        #sleep(3)
        pwmA.ChangeDutyCycle(10)
        pwmB.ChangeDutyCycle(10)
        sleep(0.5)
        
def CW_motor():
    GPIO.output(M1PHASE, GPIO.LOW)
    GPIO.output(M2PHASE, GPIO.HIGH)

    #sleep(3)
    pwmA.ChangeDutyCycle(10)
    pwmB.ChangeDutyCycle(10)
    sleep(0.5)
      
try:
    while True:
        print("Start Motor")
        
        deg45()
        sleep(0.01)
#         
#         forward()
#         sleep(4)
#         stop()
#         sleep(2)
#         backward()
#         sleep(4)
#         stop()
#         sleep(2)
#         rotate()
#         sleep(2)
#         stop()
  
        #turnLeft()
        #urnRight()
        break
    
except KeyboardInterrupt:
    
    pwmA.ChangeDutyCycle(0)
    pwmB.ChangeDutyCycle(0)
    pwmA.stop()
    pwmB.stop()
    GPIO.cleanup()
    print("Program Exit")
    
finally:
    print("Finally Stop Motor")
    pwmA.ChangeDutyCycle(0)
    pwmB.ChangeDutyCycle(0)
    pwmA.stop()
    pwmB.stop()
    GPIO.cleanup()               







