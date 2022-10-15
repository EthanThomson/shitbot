import RPi.GPIO as GPIO
import time

# GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

# set GPIO Pins
triggerfront = 18
echofront = 24
triggerback = 1
echoback = 2


# set GPIO direction (IN / OUT)
GPIO.setup(triggerfront, GPIO.OUT)
GPIO.setup(echofront, GPIO.IN)
GPIO.setup(triggerback, GPIO.OUT)
GPIO.setup(echoback, GPIO.IN)

def router(inp):

def distanceback():
    # set Trigger to HIGH
    GPIO.output(triggerback, True)

    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(triggerback, False)

    StartTime = time.time()
    StopTime = time.time()

    # save StartTime
    while GPIO.input(echoback) == 0:
        StartTime = time.time()

    # save time of arrival
    while GPIO.input(echoback) == 1:
        StopTime = time.time()

    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2

    return distance

def distancefront():
    # set Trigger to HIGH
    GPIO.output(triggerfront, True)

    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(triggerfront, False)

    StartTime = time.time()
    StopTime = time.time()

    # save StartTime
    while GPIO.input(echofront) == 0:
        StartTime = time.time()

    # save time of arrival
    while GPIO.input(echofront) == 1:
        StopTime = time.time()

    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2

    return distance


if __name__ == '__main__':
    while True:
        dist = distance()
        print ("Measured Distance = %.1f cm" % dist)
        time.sleep(1)