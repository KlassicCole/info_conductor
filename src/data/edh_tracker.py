import json
from datetime import datetime

TRACKER_FILE = 'cards.json'

def load_previous_data():
    try:
        with open(TRACKER_FILE, 'r') as f:
            data = json.load(f)
            # Ensure data is a dictionary, convert if needed
            if isinstance(data, list):
                return {}
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_data(new_cards_by_commander):
    existing_data = load_previous_data()

    for commander, new_cards in new_cards_by_commander.items():
        if commander not in existing_data:
            existing_data[commander] = []
        existing_names = {card['name'] for card in existing_data[commander]}

        for card in new_cards:
            if card['name'] not in existing_names:
                existing_data[commander].append({
                    'name': card['name'],
                    'recommended_on': datetime.now().strftime('%Y-%m-%d')
                })

    with open(TRACKER_FILE, 'w') as f:
        json.dump(existing_data, f, indent=4)

def filter_new_cards(cards_by_commander):
    existing_data = load_previous_data()
    new_cards_by_commander = {}

    for commander, cards in cards_by_commander.items():
        # Ensure the commander entry is a list, initialize if not present
        if commander not in existing_data or not isinstance(existing_data[commander], list):
            existing_data[commander] = []

        existing_names = {card['name'] for card in existing_data[commander]}
        new_cards_by_commander[commander] = [
            card for card in cards if card['name'] not in existing_names
        ]

    return new_cards_by_commander