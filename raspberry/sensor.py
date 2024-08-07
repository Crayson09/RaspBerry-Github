import RPi.GPIO as GPIO
import time
from picamera2 import Picamera2, Preview
from gpiozero import LED

number = 1
GPIO.setmode(GPIO.BCM)
PIR_PIN = 20
GPIO.setup(PIR_PIN, GPIO.IN)
led = LED(21)

picam2 = Picamera2()
camera_config = picam2.create_preview_configuration()
picam2.configure(camera_config)
picam2.start()

try:
    while True:
        if GPIO.input(PIR_PIN):
            print("Motion Detected!")
            led.on()
            time.sleep(3)
            picam2.capture_file(f"einbrecher{number}.jpg")
            print(f"Aufgenommen: einbrecher{number}.jpg")
            number += 1
            led.off()
            time.sleep(8)
        time.sleep(1)
except KeyboardInterrupt:
    print("Quit")
    GPIO.cleanup()
    picam2.close()
