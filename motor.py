
from navio.adafruit_pwm_servo_driver import PWM
import time
import math

import sys

import navio.gpio
import navio.util


class motor:
	def __init__(self, NAVIO_RCOUTPUT):
		self.NAVIO_RCOUTPUT = NAVIO_RCOUTPUT + 2 
		self.inicial = inicial
		
	navio.util.check_apm()
	
	
	#drive Output Enable in PCA low
	pin = navio.gpio.Pin(27)
	pin.write(0)

	PCA9685_DEFAULT_ADDRESS = 0x40
	frequency = 50

	#NAVIO_RCOUTPUT_1 = 3
	SERVO_MIN_ms = 1.250 # mS
	SERVO_MAX_ms = 1.750 # mS

	#Convertir mS a rango 0-4096:
	SERVO_MIN = math.trunc((SERVO_MIN_ms * 4096.0) / (1000.0 / frequency) - 1)
	SERVO_MAX = math.trunc((SERVO_MAX_ms * 4096.0) / (1000.0 / frequency) - 1)

	pwm = PWM(0x40, debug=False)

	#Set frecuencia
	pwm.setPWMFreq(frequency)
	
	def MotorOn:
		pwm.setPWM(self.NAVIO_RCOUTPUT, 0, self.SERVO_MAX);
	def MotorOff:
		pwm.setPWM(self.NAVIO_RCOUTPUT, 0, self.SERVO_MIN);
