# Bibliotheken laden
from gpiozero import LED, Button
from time import sleep

led_red = LED(26)
led_green = LED(19)
led_yellow = LED(13)
button = Button(2)

def button_pressed():
    print('You pushed me')
    print("Pressed")
    sleep(2)


button.when_pressed = button_pressed

# Main loop to keep the program running
while True:
    sleep(1)
