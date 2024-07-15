# Bibliotheken laden
from gpiozero import LED
from time import sleep

# Initialisierung von GPIO17 als LED (Ausgang)
led = LED(26)

# LED einschalten
led.on()
print("Licht an)")
# 5 Sekunden warten
sleep(5)

# LED ausschalten
led.off()
print("Licht aus")