import RPi.GPIO as GPIO
import time

from gpiozero import LED

GPIO.setmode(GPIO.BCM)
PIR_PIN = 20
GPIO.setup(PIR_PIN, GPIO.IN)
led = LED(21)
try:
    while True:
        if GPIO.input(PIR_PIN):
            print("Motion Detected!")
            led.on()
            time.sleep(1)
            led.off()
            time.sleep(8)
        time.sleep(1)
except KeyboardInterrupt:
    print("Quit")
    GPIO.cleanup()
