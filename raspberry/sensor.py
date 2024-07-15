import RPi.GPIO as GPIO
import time

SENSOR_PIN = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN, GPIO.IN)

def mein_callback(channel):
    print('Es gab eine Bewegung!')

try:
    GPIO.add_event_detect(SENSOR_PIN, GPIO.RISING, callback=mein_callback)
    print('Warte auf Bewegung...')
    while True:
        time.sleep(1)  # Reduced sleep time for responsiveness
except KeyboardInterrupt:
    print("\nBeende...")
finally:
    GPIO.cleanup()
