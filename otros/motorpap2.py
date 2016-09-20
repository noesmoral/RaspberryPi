#!/usr/bin/env python
 
# import required libs
import time
import RPi.GPIO as GPIO

GPIO.cleanup() #cleaning up in case GPIOS have been preactivated
 
# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)
 
# be sure you are setting pins accordingly
# GPIO10,GPIO9,GPIO11,GPI25
StepPins = [10,9,11,25]
 
# Set all pins as output
for pin in StepPins:
  GPIO.setup(pin,GPIO.OUT)
  GPIO.output(pin, False)

#wait some time to start
time.sleep(0.5)
 
# Define some settings
StepCounter = 0
WaitTime = 0.0015

# Full giro anti horario
Seq1 = []
Seq1 = range(0, 4)
Seq1[0] = [1,1,0,0]
Seq1[1] = [1,0,0,1]
Seq1[2] = [0,0,1,1]
Seq1[3] = [0,1,1,0]
 
# Define advanced sequence
# medio giro horario
Seq2 = []
Seq2 = range(0, 8)
Seq2[0] = [1,0,0,0]
Seq2[1] = [1,1,0,0]
Seq2[2] = [0,1,0,0]
Seq2[3] = [0,1,1,0]
Seq2[4] = [0,0,1,0]
Seq2[5] = [0,0,1,1]
Seq2[6] = [0,0,0,1]
Seq2[7] = [1,0,0,1]

# medio giro anti horario
Seq4 = []
Seq4 = range(0, 8)
Seq4[0] = [1,0,0,0]
Seq4[1] = [1,0,0,1]
Seq4[2] = [0,0,0,1]
Seq4[3] = [0,0,1,1]
Seq4[4] = [0,0,1,0]
Seq4[5] = [0,1,1,0]
Seq4[6] = [0,1,0,0]
Seq4[7] = [1,1,0,0]

#Full torque giro horario
Seq3 = []
Seq3 = [3,2,1,0]
Seq3[0] = [0,0,1,1]
Seq3[1] = [1,0,0,1]
Seq3[2] = [1,1,0,0]
Seq3[3] = [0,1,1,0]


def girarIF(aux):
	StepCounter=0
	print(aux*8)
	for x in range(1,aux*8):
		print("El valor de x es ",x)
		for z in range(0, 4):
			print("el valor de z es ",z)
			xpin2 = StepPins[z]
			print("el valor de pin es ",xpin2)
			print("el contador es ",StepCounter)
			print(Seq1[StepCounter][z])
			if Seq1[StepCounter][z]==1:
				print " Step %i Enable %i" %(StepCounter,xpin2)
				GPIO.output(xpin2, True)
			else:
				GPIO.output(xpin2, False)
		print("6")
		StepCounter = StepCounter+1
		print("7")
		if (StepCounter==4):
			StepCounter = 0
		if (StepCounter<0):
			StepCounter = 0
		# Wait before moving on
		time.sleep(WaitTime)

def girarIM(aux):
	StepCounter=0
	print(aux*8)
	for x in range(1,aux*8):
		print("El valor de x es ",x)
		for z in range(0, 4):
			print("el valor de z es ",z)
			xpin2 = StepPins[z]
			print("el valor de pin es ",xpin2)
			print("el contador es ",StepCounter)
			print(Seq4[StepCounter][z])
			if Seq4[StepCounter][z]==1:
				print " Step %i Enable %i" %(StepCounter,xpin2)
				GPIO.output(xpin2, True)
			else:
				GPIO.output(xpin2, False)
		print("6")
		StepCounter = StepCounter+1
		print("7")
		if (StepCounter==8):
			StepCounter = 0
		if (StepCounter<0):
			StepCounter = 0
		# Wait before moving on
		time.sleep(WaitTime)
 
def girarDF(aux):
	StepCounter=0
	for x in range(1,aux*8):
		for z in range(0, 4):
			xpin2 = StepPins[z]
			if Seq1[StepCounter][z]==1:
				print " Step %i Enable %i" %(StepCounter,xpin2)
				GPIO.output(xpin2, True)
			else:
				GPIO.output(xpin2, False)
		StepCounter = StepCounter+1
		if (StepCounter==4):
			StepCounter = 0
		if (StepCounter<0):
			StepCounter = 0
		# Wait before moving on
		time.sleep(WaitTime)

def girarDM(aux):
	StepCounter=0
	for x in range(1,aux*8):
		for z in range(0, 4):
			xpin2 = StepPins[z]
			if Seq4[StepCounter][z]==1:
				print " Step %i Enable %i" %(StepCounter,xpin2)
				GPIO.output(xpin2, True)
			else:
				GPIO.output(xpin2, False)
		StepCounter = StepCounter+1
		if (StepCounter==8):
			StepCounter = 0
		if (StepCounter<0):
			StepCounter = 0
		# Wait before moving on
		time.sleep(WaitTime)


# Start main loop
try:
	while 1==1:
  		print("Selecciona cantidad de movimiento:")
		movimiento=raw_input()
		movimiento=int(movimiento)
		print("Selecciona direccion izquierda(izq) o derecha(der):")
		direccion=raw_input()
		if direccion=="izq":
			print("Selecciona velocidad media(med) o rapida(fast):")
			velocidad=raw_input();
			if velocidad=="med":
				girarIM(movimiento)
			else:
				girarIF(movimiento)
		else:
			print("Selecciona velocidad media(1) o rapida(2):")
			velocidad=raw_input();
			if velocidad=='med':
				girarDM(movimiento)
			else:
				girarDF(movimiento)
		for pin in StepPins:
			GPIO.output(pin, False)				
except:
  GPIO.cleanup();
finally: #cleaning up and setting pins to low again (motors can get hot if you wont) 
  GPIO.cleanup();
  for pin in StepPins:
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin, False)