import requests
from bs4 import BeautifulSoup
import os

COMMANDER_URL = 'https://edhrec.com/commanders/atraxa-praetors-voice/planeswalkers'

def scrape_commander_cards(url):
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to fetch the page.")
        return []

    soup = BeautifulSoup(response.content, 'lxml')
    new_card_container = soup.find('div', id='newcards')

    if not new_card_container:
        print("No new card container found.")
        return []

    cards = []
    card_elements = new_card_container.find_all('div', class_='d-flex justify-content-center mb-2')

    for card in card_elements:
        card_name = card.text.strip() or "Unnamed Card"
        img_tag = card.find('img')
        img_url = img_tag['src'] if img_tag else None
        cards.append({'name': card_name, 'img_url': img_url})

    return cards
