# Bibliotheken laden
from gpiozero import LED
from time import sleep

led = LED(26)

led.on()
sleep(5)
led.blink()
sleep(5)
led.off()
