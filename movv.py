import wiringpi
import time

# Motor speeds for this library are specified as numbers
# between -MAX_SPEED and MAX_SPEED, inclusive.
_max_speed = 480  # 19.2 MHz / 2 / 480 = 20 kHz
MAX_SPEED = _max_speed

io_initialized = False
def io_init():
  global io_initialized
  if io_initialized:
    return

  wiringpi.wiringPiSetupGpio()
  wiringpi.pinMode(15, wiringpi.GPIO.PWM_OUTPUT)
  wiringpi.pinMode(25, wiringpi.GPIO.PWM_OUTPUT)

  wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)
  wiringpi.pwmSetRange(MAX_SPEED)
  wiringpi.pwmSetClock(2)

  wiringpi.pinMode(14, wiringpi.GPIO.OUTPUT)
  wiringpi.pinMode(24, wiringpi.GPIO.OUTPUT)

  io_initialized = True

class Motor(object):
    MAX_SPEED = _max_speed

    def __init__(self, pwm_pin, dir_pin):
        self.pwm_pin = pwm_pin
        self.dir_pin = dir_pin

    def setSpeed(self, speed):
        if speed < 0:
            speed = -speed
            dir_value = 1
        else:
            dir_value = 0

        if speed > MAX_SPEED:
            speed = MAX_SPEED

        io_init()
        wiringpi.digitalWrite(self.dir_pin, dir_value)
        wiringpi.pwmWrite(self.pwm_pin, speed)

class Motors(object):
    MAX_SPEED = _max_speed

    def __init__(self):
        self.motor1 = Motor(12, 5)
        self.motor2 = Motor(13, 6)

    def setSpeeds(self, m1_speed, m2_speed):
        self.motor1.setSpeed(m1_speed)
        self.motor2.setSpeed(m2_speed)

motors = Motors()






# Set up sequences of motor speeds.
test_forward_speeds = list(range(0, MAX_SPEED, 1)) + \
  [MAX_SPEED] * 200 + list(range(MAX_SPEED, 0, -1)) + [0]

test_reverse_speeds = list(range(0, -MAX_SPEED, -1)) + \
  [-MAX_SPEED] * 200 + list(range(-MAX_SPEED, 0, 1)) + [0]

motors.setSpeeds(0, 0)

print("Motor 1 forward")
for s in test_forward_speeds:
    motors.motor1.setSpeed(s)
    time.sleep(0.005)

print("Motor 1 reverse")
for s in test_reverse_speeds:
    motors.motor1.setSpeed(s)
    time.sleep(0.005)

print("Motor 2 forward")
for s in test_forward_speeds:
    motors.motor2.setSpeed(s)
    time.sleep(0.005)

print("Motor 2 reverse")
for s in test_reverse_speeds:
    motors.motor2.setSpeed(s)
    time.sleep(0.005)
