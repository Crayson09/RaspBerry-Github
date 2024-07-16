from gpiozero import LED, Button
from time import sleep
import random

# Initialisierung
led_green = LED(19)
button = Button(2)
button_2 = Button(3)
button_3 = Button(4)

def button_pressed():
    print("Pressed:1")


def button_pressed_2():
    print("Pressed:2")


def button_pressed_3():
    print("Pressed:3")
# Event-Handler zuweisen
button.when_pressed = button_pressed
button_2.when_pressed = button_pressed_2
button_3.when_pressed = button_pressed_3
# Hauptschleife
while True:
    sleep(1)
