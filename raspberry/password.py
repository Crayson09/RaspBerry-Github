from gpiozero import LED, Button
from time import sleep

# Initialisierung
led_green = LED(19)
button = Button(2)
button_2 = Button(3)
button_3 = Button(4)

# Festlegen der korrekten Reihenfolge der Tastendrücke
correct_sequence = [1, 1, 3, 2]
current_sequence = []


def check_sequence():
    global current_sequence

    if current_sequence == correct_sequence:
        print("YES")
        # Hier kannst du weitere Aktionen ausführen, z.B. LED einschalten
        led_green.on()
        current_sequence.clear()
    elif len(current_sequence) >= 4:
        print("falsch")
        current_sequence.clear()
        exit()


# Event-Handler zuweisen
def button_pressed(button_num):
    global current_sequence
    current_sequence.append(button_num)
    check_sequence()


button.when_pressed = lambda: button_pressed(1)
button_2.when_pressed = lambda: button_pressed(2)
button_3.when_pressed = lambda: button_pressed(3)

# Hauptschleife
try:
    while True:
        sleep(1)

finally:
    led_green.off()  # LED ausschalten, wenn das Programm beendet wird
