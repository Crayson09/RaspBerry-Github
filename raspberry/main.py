# Bibliotheken laden
from gpiozero import LED, Button
from time import sleep
import random
led_green = LED(19)
button = Button(2)
button_2 = Button(4)
def button_pressed():
    print('2')
    led_green.on()
    sleep(2)
    led_green.off()


def button_pressed_2():
    print("1")
    led_green.on()
    sleep(2)
    led_green.off()

button.when_pressed = button_pressed
button_2.when_pressed = button_pressed_2
# Main loop to keep the program running
while True:
    sleep(1)
