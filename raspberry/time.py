import argparse
import schedule
import time

# Funktion zum Ausgeben der Nachricht mit variablem Inhalt
def print_custom_message(content):
    print(f"{content}")

# Funktion zum Hinzufügen neuer Zeitpläne
def add_new_schedule(day, hour, minute, job, content):
    schedule.every().day.at(f"{hour:02}:{minute:02}").do(job, content)

# Funktion zum Parsen von Kommandozeilenargumenten
def parse_arguments():
    parser = argparse.ArgumentParser(description="Fügt einen neuen Zeitplan für eine automatische Nachricht hinzu.")
    parser.add_argument("day", choices=["every", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"], help="Tag des Zeitplans")
    parser.add_argument("hour", type=int, help="Stunde des Zeitplans (0-23)")
    parser.add_argument("minute", type=int, help="Minute des Zeitplans (0-59)")
    parser.add_argument("content", help="Inhalt der automatischen Nachricht")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()
    add_new_schedule(args.day, args.hour, args.minute, print_custom_message, args.content)

    # Endlosschleife zum Überprüfen des Zeitplans
    while True:
        schedule.run_pending()
        time.sleep(1)
