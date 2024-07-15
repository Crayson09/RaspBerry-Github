import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
PIN = 21
GPIO.setup(PIN, GPIO.IN)

print ("HC-SR505 Bewegungssensor starten...")
time.sleep(2)
print ("Bewegungssensor aktiviert...")

while True:
   if GPIO.input(PIN):
      print ("Bewegung erkannt am " + (time.strftime("%H:%M:%S")))
      time.sleep(9)
   time.sleep(1)