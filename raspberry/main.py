from gpiozero import LED, Button
from time import sleep
import random
import sys

# Initialisierung
led_green = LED(19)
button = Button(2)
button_2 = Button(4)
random_time = random.randint(5, 20)

# Variable für den LED-Zustand
leuchtet = False

def button_pressed():
    global leuchtet
    if leuchtet:
        led_green.off()
        print("Spieler 2 hat gewonnen")
        leuchtet = False
        sys.exit()  # Beendet das Programm

def button_pressed_2():
    global leuchtet
    if leuchtet:
        led_green.off()
        print("Spieler 1 hat gewonnen")
        leuchtet = False
        sys.exit()  # Beendet das Programm

# Event-Handler zuweisen
button.when_pressed = button_pressed
button_2.when_pressed = button_pressed_2

# Hauptschleife
while True:
    sleep(random_time)
    led_green.on()
    leuchtet = True

    