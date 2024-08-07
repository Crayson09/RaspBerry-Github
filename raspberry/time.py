import argparse
import schedule
import time
import requests
from datetime import datetime

# Discord Webhook URL einfügen
DISCORD_WEBHOOK_URL = 'https://discord.com/api/webhooks/1262681444568928298/D0ntYqkalDdLVD6An7XLoSlzK-7qPeLmpu5Mq76ws07J39dHtwTX4r2LktK1J0h0Kmvs'


# Funktion zum Senden der Nachricht als Embed über Discord-Webhook
def send_discord_embed(content):
    current_time = datetime.now().strftime('%H:%M:%S')

    embed = {
        'title': 'Automatische Nachricht',
        'description': content,
        'color': 0x00ff00,  # Grün (kann angepasst werden)
        'footer': {
            'text': f'Ausgelöst um {current_time}'
        }
    }

    data = {
        'content': '',
        'embeds': [embed]
    }

    try:
        response = requests.post(DISCORD_WEBHOOK_URL, json=data)
        response.raise_for_status()
        print('Nachricht erfolgreich als Embed über Discord-Webhook gesendet!')
    except requests.exceptions.RequestException as e:
        print(f'Fehler beim Senden der Nachricht als Embed über Discord-Webhook: {e}')


# Funktion zum Hinzufügen neuer Zeitpläne
def add_new_schedule(day, hour, minute, job, content):
    schedule.every().day.at(f"{hour:02}:{minute:02}").do(job, content)


# Funktion zum Parsen von Kommandozeilenargumenten
def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Fügt einen neuen Zeitplan für eine automatische Nachricht über Discord als Embed hinzu.")
    parser.add_argument("day",
                        choices=["every", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"],
                        help="Tag des Zeitplans")
    parser.add_argument("hour", type=int, help="Stunde des Zeitplans (0-23)")
    parser.add_argument("minute", type=int, help="Minute des Zeitplans (0-59)")
    parser.add_argument("content", help="Inhalt der automatischen Nachricht")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()
    add_new_schedule(args.day, args.hour, args.minute, send_discord_embed, args.content)

    # Endlosschleife zum Überprüfen des Zeitplans
    while True:
        schedule.run_pending()
        time.sleep(1)
