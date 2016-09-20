import ejex
import ejey
import lcd
import threading

# import required libs
import time
import RPi.GPIO as GPIO

#GPIO.cleanup() #cleaning up in case GPIOS have been preactivated
 
# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
 
# be sure you are setting pins accordingly
# GPIO10,GPIO9,GPIO11,GPI25
StepPinsX = [10,9,11,25]
StepPinsY = [17,27,22,18]

# Define GPIO to LCD mapping
LCD_RS = 3
LCD_E  = 4
LCD_D4 = 23
LCD_D5 = 24
LCD_D6 = 8
LCD_D7 = 7

# Set all pins as output
for pin in StepPinsX:
  GPIO.setup(pin,GPIO.OUT)
  GPIO.output(pin, False)

# Set all pins as output
for pin in StepPinsY:
  GPIO.setup(pin,GPIO.OUT)
  GPIO.output(pin, False)

#set all pins as output
GPIO.setup(LCD_E,  GPIO.OUT)  # E
GPIO.setup(LCD_RS, GPIO.OUT) # RS
GPIO.setup(LCD_D4, GPIO.OUT) # DB4
GPIO.setup(LCD_D5, GPIO.OUT) # DB5
GPIO.setup(LCD_D6, GPIO.OUT) # DB6
GPIO.setup(LCD_D7, GPIO.OUT) # DB7

#declaracion de felocidad true a media false a full
modoVelocidad=True
 
#definition line lcd 
LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line

mensajeX="Eje X en "
mensajeY="Eje Y en "

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
	lcd.lcd_init()
	lcd.lcd_string("Eje X en 0",LCD_LINE_1)
	lcd.lcd_string("Eje Y en 0",LCD_LINE_2)

	while 1==1:
  		print("Seleccion movimiento en eje x actualmente en",cx)
		movimientox=raw_input()
		movimientox=int(movimientox)
		cx=movimientox-cx;
		print("Seleccion movimiento en eje y actualmente en",cy)
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
		aux1=mensajeX+str(cx)
		aux2=mensajeY+str(cy)
		lcd.lcd_string(aux1,LCD_LINE_1)
		lcd.lcd_string(aux2,LCD_LINE_2)
except:
	lcd.lcd_string("Goodbye, See",LCD_LINE_1)
	lcd.lcd_string("You next time!",LCD_LINE_2)
	cx=0-cx;
  	tx = threading.Thread(target=mandarMoverX, args=(cx,))
  	tx.start()
  	cy=0-cy;
  	ty = threading.Thread(target=mandarMoverY, args=(cy,))
  	ty.start()
  	tx.join()
  	ty.join()
	
	lcd.lcd_init()
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