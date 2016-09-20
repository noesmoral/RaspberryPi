import RPi.GPIO as GPIO    #Importamos la libreria RPi.GPIO
import time                #Importamos time para poder usar time.sleep

GPIO.setmode(GPIO.BCM)   #Ponemos la Raspberry en modo BOARD
GPIO.setup(14,GPIO.OUT)    #Ponemos el pin 21 como salida
p = GPIO.PWM(14,50)        #Ponemos el pin 21 en modo PWM y enviamos 50 pulsos por segundo
p.start(2.5)               #Enviamos un pulso del 7.5% para centrar el servo


try:               
    while True:      #iniciamos un loop infinito
    	
    	p.ChangeDutyCycle(2.5)    #Enviamos un pulso del 4.5% para girar el servo hacia la izquierda
    	time.sleep(0.5)           #pausa de medio segundo
		p.ChangeDutyCycle(5.0)    #Enviamos un pulso del 4.5% para girar el servo hacia la izquierda
		time.sleep(0.5)           #pausa de medio segundo
		p.ChangeDutyCycle(7.5)    #Enviamos un pulso del 4.5% para girar el servo hacia la izquierda
		time.sleep(0.5)           #pausa de medio segundo
		p.ChangeDutyCycle(10.0)    #Enviamos un pulso del 4.5% para girar el servo hacia la izquierda
		time.sleep(0.5)           #pausa de medio segundo
		p.ChangeDutyCycle(12.5)    #Enviamos un pulso del 4.5% para girar el servo hacia la izquierda
		time.sleep(0.5)           #pausa de medio segundo


except KeyboardInterrupt:         #Si el usuario pulsa CONTROL+C entonces...
    p.stop()                      #Detenemos el servo 
    GPIO.cleanup()                #Limpiamos los pines GPIO de la Raspberry y cerramos el script