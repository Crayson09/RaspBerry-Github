from machine import Pin
import utime
led = Pin(21, Pin.OUT)
pir = Pin(20, Pin.IN, Pin.PULL_UP)
led.low()
utime.sleep(3)
while True:
   print(pir.value())
   if pir.value() == 0:
       print("LED On")
       led.high()
       utime.sleep(5)
   else:
       print("Waiting for movement")
       led.low()
utime.sleep(0.2)