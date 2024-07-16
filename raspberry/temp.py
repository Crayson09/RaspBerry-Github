import Adafruit_DHT

# Wähle den Sensortyp aus
sensor = Adafruit_DHT.DHT22

# GPIO-Pin, an dem der Data-Pin des Sensors angeschlossen ist
pin = 21

# Lese die Temperatur- und Feuchtigkeitsdaten
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

if humidity is not None and temperature is not None:
    print(f'Temperatur: {temperature:.1f}°C')
    print(f'Luftfeuchtigkeit: {humidity:.1f}%')
else:
    print('Fehler beim Auslesen des Sensors')
