import RPi.GPIO as GPIO
import time

from gpiozero import LED

GPIO.setmode(GPIO.BOARD)
PIN = 21
GPIO.setup(PIN, GPIO.IN)
led = LED(20)

print ("HC-SR505 Bewegungssensor starten...")
time.sleep(2)
print ("Bewegungssensor aktiviert...")

while True:
   if GPIO.input(PIN):
      print ("Bewegung erkannt am " + (time.strftime("%H:%M:%S")))
      led.blink()
      time.sleep(9)
   time.sleep(1)