from gpiozero import LED, Button
from time import sleep
import random

# Initialisierung
led_green = LED(19)
button = Button(2)
button_2 = Button(3)
random_time = random.randint(5, 20)


# Variable für den LED-Zustand und Programmstatus
leuchtet = False
running = True

def button_pressed():
    global leuchtet, running
    print("Pressed 1")
    if leuchtet:
        led_green.off()
        print("Spieler 2 hat gewonnen")
        leuchtet = False
        running = False  # Beendet das Programm

def button_pressed_2():
    global leuchtet, running
    print("Pressed 2")
    if leuchtet:
        led_green.off()
        print("Spieler 1 hat gewonnen")
        leuchtet = False
        running = False  # Beendet das Programm

# Event-Handler zuweisen
button.when_pressed = button_pressed
button_2.when_pressed = button_pressed_2

# Hauptschleife
while running:
    sleep(random_time)
    led_green.on()
    leuchtet = True



print("Programm beendet")
