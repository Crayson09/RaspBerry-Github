from datetime import datetime

import requests
from gpiozero import LED, Button
from time import sleep

# Initialisierung
button = Button(2)
button_2 = Button(3)
button_3 = Button(4)
API_KEY = "1/IiNKjbAhAujqG+1LXrgg==vbSXA952hGx7yj6f"
# Festlegen der korrekten Reihenfolge der Tastendrücke
correct_sequence = [1, 1, 3, 2,1,3]
current_sequence = []
DISCORD_WEBHOOK_URL = 'https://discord.com/api/webhooks/1262681444568928298/D0ntYqkalDdLVD6An7XLoSlzK-7qPeLmpu5Mq76ws07J39dHtwTX4r2LktK1J0h0Kmvs'

def print_quote(quote, author, category):
    print(f'Kategorie: {category}')
    print(f'"{quote}"')
    print(f'- {author}')
    print()

# Funktion zum Senden der Nachricht als Embed über Discord-Webhook
def send_discord_embed(content,falsch):
    current_time = datetime.now().strftime('%H:%M:%S')
    if falsch:
        embed = {
            'title': 'Neuer versuchter Login',
            'description': content,
            'color': 880000,  # Grün (kann angepasst werden)
            'footer': {
                'text': f'Ausgelöst um {current_time}'
            }
        }
    else:
        embed = {
            'title': 'Neuer  Login',
            'description': content,
            'color': "008800",  # Grün (kann angepasst werden)
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
    except requests.exceptions.RequestException as e:
        print(f'Fehler beim Senden der Nachricht als Embed über Discord-Webhook: {e}')


def check_sequence():
    global current_sequence

    if current_sequence == correct_sequence:
        print("Passcode war richtig")
        print("--------------------------------------------------")
        print("Coming soon")
        api_url = 'https://api.api-ninjas.com/v1/quotes'
        params = {
            'category': 'random'  # Zufällige Zitate aus verschiedenen Kategorien erhalten
        }
        headers = {
            'X-Api-Key': API_KEY
        }
        ip_address = requests.get('https://api64.ipify.org').text
        send_discord_embed(ip_address,falsch=False)
        try:
            response = requests.get(api_url, params=params, headers=headers)
            response.raise_for_status()
            quote_data = response.json()  # Erste Zitat aus der Antwort abrufen

            quote = quote_data['quote']
            author = quote_data['author']
            category = quote_data['category']

            print_quote(quote, author, category)
        except requests.exceptions.RequestException as e:
            print(f'Fehler beim Abrufen eines Zitats von der API: {e}')
        # Hier kannst du weitere Aktionen ausführen, z.B. LED einschalten
        current_sequence.clear()
    elif len(current_sequence) >= 6:
        print("Falsch | Programm bitte neustarten")
        ip_address = requests.get('https://api64.ipify.org').text
        send_discord_embed(ip_address,falsch=True)
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
while True:
    sleep(1)
