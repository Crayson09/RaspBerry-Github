from picamera2 import Picamera2, Preview
from time import sleep
from gpiozero import LED, Button
button = Button(2)


def button_pressed():
    print("Gedrückt")
    picam2 = Picamera2()
    camera_config = picam2.create_preview_configuration()
    picam2.configure(camera_config)
    picam2.start()
    sleep(1)
    picam2.capture_file("button_pressed.jpg")


button.when_pressed = button_pressed




while True:
    sleep(1)

