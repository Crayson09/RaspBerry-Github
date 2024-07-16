import schedule
import time

# Funktion zum Ausgeben der Nachricht
def print_message():
    print("Hier ist deine automatische Nachricht!")

# Zeitplan festlegen (Beispiel: Jeden Tag um 9:46 Uhr)
schedule.every().day.at("09:47").do(print_message)

# Endlosschleife zum Überprüfen des Zeitplans
while True:
    schedule.run_pending()
    time.sleep(1)
