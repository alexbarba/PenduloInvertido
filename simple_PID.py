# coding=utf-8
#import IMU.py
import pruebas
import IMU
import motor

def pid_controller(P=1, I=1, D=1):
	
	
	T=1		#Periodo
	numlecturas = 10
	#lecturas=[0]*numlecturas
	
	
	#Inicialización
	ui_prev = 0
	e_prev = 0
	e_acumulado = 0
	ti = time.clock() #tiempo inicial
	Referencia = 0
	
	#Actuadores
	motor1=motor.motor(1)
	motor2=motor.motor(2)
	
	#IMU
	imu1=IMU.IMU()
	
	while True:
		# Error between the desired and actual output
		ta=time.clock()
		sensor = 0
		for i in range(numlecturas):
			sensor += imu1.SetAcc[1]
			i+=1
		sensor /= numlecturas
		
		if ta - ti >= T:
			e_actual = sensor - Referencia
			e_acumulado += e_actual
			diferencia_e = e_actual - e_prev
			
			control_PID = e_actual * P + e_acumulado * I + diferencia_e * D
			
			

			# Adjust previous values
			e_prev = e_actual
			ti = time.clock()

			#k += 1

		
