import OPi.GPIO as GPIO # OPi.GPIO is the OPi version of gpiozero, a RPi library
import time


class Pikachu:
    GPIO.setmode(GPIO.SUNXI)
    GPIO.setwarnings(False)

    def __init__(self):
        self.motor1 = 'PA8'
        self.motor2 = 'PA9'
        self.motor3 = 'PA10'
        self.motor4 = 'PA20'
        GPIO.setup(self.motor1, GPIO.OUT)
        GPIO.setup(self.motor2, GPIO.OUT)
        GPIO.setup(self.motor3, GPIO.OUT)
        GPIO.setup(self.motor4, GPIO.OUT)

    def moveForward(self):
        GPIO.output(self.motor1, 1)
        GPIO.output(self.motor2, 1)
        GPIO.output(self.motor3, 1)
        GPIO.output(self.motor4, 1)
        GPIO.PWM(self.motor1, 20)
        GPIO.PWM(self.motor2, 20)
        GPIO.PWM(self.motor3, 20)
        GPIO.PWM(self.motor4, 20)

        time.sleep(2) # Wait 2 seconds

        GPIO.output(self.motor1, 0)
        GPIO.output(self.motor2, 0)
        GPIO.output(self.motor3, 0)
        GPIO.output(self.motor4, 0)
        GPIO.PWM(self.motor1, 0)
        GPIO.PWM(self.motor2, 0)
        GPIO.PWM(self.motor3, 0)
        GPIO.PWM(self.motor4, 0)