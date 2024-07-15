# Bibliotheken laden
from gpiozero import LED, Button
from time import sleep
import random
led_green = LED(19)
button = Button(2)
button_2 = Button(4)
random_time = random.randint(15,30)
def button_pressed():
    print('2')



def button_pressed_2():
    print("1")


button.when_pressed = button_pressed
button_2.when_pressed = button_pressed_2
while True:
    sleep(random_time)
    led_green.on()
