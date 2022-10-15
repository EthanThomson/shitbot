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


pwmA = GPIO.PWM(M1ENABLE, 1000)
pwmB = GPIO.PWM(M2ENABLE, 1000)

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
    pwmA.ChangeDutyCycle(10)
    pwmB.ChangeDutyCycle(10)
    sleep(0.5)    

    
def backward():
    print("Motor Backword")
    GPIO.output(M1PHASE, GPIO.HIGH)
    GPIO.output(M2PHASE, GPIO.HIGH)

    #sleep(3)
    pwmA.ChangeDutyCycle(0.5)
    pwmB.ChangeDutyCycle(0.5)
#     sleep(3)
    
    
# def main():
#     
#     while True:
#         
#         #forward()
#         #backward()
#         LineFollower()
#         sleep(0.1)
#         MotorDirection() 
 
try:
    while True:

        #forward()
        #backward()
        LineFollower()
        sleep(0.1)
        MotorDirection() 

        ("Start Motor")


except KeyboardInterrupt:
        
    pwmA.ChangeDutyCycle(0)
    pwmB.ChangeDutyCycle(0)
    pwmA.stop()
    pwmB.stop()
    GPIO.cleanup()
    print("MOTOR STOP")
