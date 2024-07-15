# Bibliotheken laden
from gpiozero import LED,Button
from time import sleep

led_red = LED(26)
led_green = LED(19)
led_yellow = LED(13)
button = Button(5)
button.when_pressed = led_yellow.on
button.when_released = led_yellow.off
led_red.on()
if button.is_held:
    sleep(5)
    led_red.off()
    led_yellow.on()
    sleep(1)
    led_yellow.off()
    led_red.off()
    led_green.on()
    sleep(5)
    led_yellow.on()
    sleep(1)
    led_yellow.off()
    led_red.on()
    led_green.off()
