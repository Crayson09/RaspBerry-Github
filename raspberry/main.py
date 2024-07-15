# Bibliotheken laden
from gpiozero import LED, Button
from time import sleep

led_green = LED(19)
button = Button(2)

def button_pressed():
    print('You pushed me')
    print("Pressed")
    led_green.on()
    sleep(2)
    led_green.off()

button.when_pressed = button_pressed

# Main loop to keep the program running
while True:
    sleep(1)
