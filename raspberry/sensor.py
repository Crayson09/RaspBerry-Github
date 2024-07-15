import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
PIN = 21
GPIO.setup(PIN, GPIO.IN)

print ("Start HC-SR505 bewegingssensor...")
time.sleep(2)
print ("Bewegingssensor geactiveerd...")

while True:
   if GPIO.input(PIN):
      print ("Beweging gedetecteerd op " + (time.strftime("%H:%M:%S")))
      time.sleep(9)
   time.sleep(1)