import spidev
import time
import sys
import navio.util
from navio.mpu9250 import MPU9250

class IMU:
	navio.util.check_apm()

	imu = MPU9250()

	if imu.testConnection():
		print "IMU conectado correctamente"
	else: 
		sys.exit("IMU no funciona")

	imu.initialize()
	
	
	def SetAcc(self):
		m9a, m9g, m9m = self.imu.getMotion9()
		return "{:+7.3f}".format(m9a[0]), "{:+7.3f}".format(m9a[1]), "{:+7.3f}".format(m9a[2])
	def SetGyr(self):
		m9a, m9g, m9m = self.imu.getMotion9()
		return "{:+8.3f}".format(m9g[0]), "{:+8.3f}".format(m9g[1]), "{:+8.3f}".format(m9g[2])
	def SetMag(self):
		m9a, m9g, m9m = self.imu.getMotion9()
		return "{:+7.3f}".format(m9m[0]), "{:+7.3f}".format(m9m[1]), "{:+7.3f}".format(m9m[2])
