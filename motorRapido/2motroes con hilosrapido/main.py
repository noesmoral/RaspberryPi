import ejex
import ejey
import threading

# import required libs
import time
import RPi.GPIO as GPIO

#GPIO.cleanup() #cleaning up in case GPIOS have been preactivated
 
# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)
 
# be sure you are setting pins accordingly
# GPIO10,GPIO9,GPIO11,GPI25
StepPinsX = [10,9,11,25]
StepPinsY = [17,27,22,18]

 
# Set all pins as output
for pin in StepPinsX:
  GPIO.setup(pin,GPIO.OUT)
  GPIO.output(pin, False)

# Set all pins as output
for pin in StepPinsY:
  GPIO.setup(pin,GPIO.OUT)
  GPIO.output(pin, False)

#declaracion de felocidad true a media false a full
modoVelocidad=False

def mandarMoverX(mov):
	if modoVelocidad==True:
		if mov<0:
			ejex.girarIM(-mov)
		else:
			ejex.girarDM(mov)
	else:
		if mov<0:
			ejex.girarIF(-mov)
		else:
			ejex.girarDF(mov)

def mandarMoverY(mov):
	if modoVelocidad==True:
		if mov<0:
			ejey.girarIM(-mov)
		else:
			ejey.girarDM(mov)
	else:
		if mov<0:
			ejey.girarIF(-mov)
		else:
			ejey.girarDF(mov)


# Start main loop
try:
	#inicializo las cordenadas a 0 en los dos ejes en caso de montarlo seria necesario un reset para ir a esa posicion
	cx=0
	cy=0
	while 1==1:
  		print("Seleccion movimiento en eje x actualmente en %d: ",cx)
		movimientox=raw_input()
		movimientox=int(movimientox)
		cx=movimientox-cx;
		print("Seleccion movimiento en eje y actualmente en %d: ",cy)
		movimientoy=raw_input()
		movimientoy=int(movimientoy)
		cy=movimientoy-cy;
		tx = threading.Thread(target=mandarMoverX, args=(cx,))
		tx.start()
		ty = threading.Thread(target=mandarMoverY, args=(cy,))
		ty.start()
		tx.join()
		ty.join()
		cx=movimientox
		cy=movimientoy
except:
	cx=0-cx;
  	tx = threading.Thread(target=mandarMoverX, args=(cx,))
  	tx.start()
  	cy=0-cy;
  	ty = threading.Thread(target=mandarMoverY, args=(cy,))
  	ty.start()
  	tx.join()
  	ty.join()
finally: #cleaning up and setting pins to low again (motors can get hot if you wont) 
  	GPIO.cleanup();
  	#ejex.cerrar();
  	#ejey.cerrar();
  	for pin in StepPinsX:
  		GPIO.setup(pin,GPIO.OUT)
  		GPIO.output(pin, False)
  	for pin in StepPinsY:
  		GPIO.setup(pin,GPIO.OUT)
  		GPIO.output(pin, False)
