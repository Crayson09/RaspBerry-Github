# Bibliotheken laden
from gpiozero import LED
from time import sleep

led_red = LED(26)
led_green = LED(19)

led_red.on()
sleep(5)
led_red.off()
led_green.on()
sleep(5)
led_red.on()
led_green.off()
