from scraper import scrape_commander_cards
from tracker import filter_new_cards, save_data
from emailer import send_email

COMMANDER_URLS = {
    'Atraxa, Praetors Voice': 'https://edhrec.com/commanders/atraxa-praetors-voice/planeswalkers',
    'Gargos Vicious Watcher': 'https://edhrec.com/commanders/gargos-vicious-watcher',
    'Krenko, Mob Boss': 'https://edhrec.com/commanders/krenko-mob-boss',
    'Liberator Urzas Battlethopter': 'https://edhrec.com/commanders/liberator-urzas-battlethopter',
    'Ghyrson Starn Kelermorph': 'https://edhrec.com/commanders/ghyrson-starn-kelermorph',
    'Kenrith the Returned King': 'https://edhrec.com/commanders/kenrith-the-returned-king/group-hug',
    'The First Sliver': 'https://edhrec.com/commanders/the-first-sliver'
}

if __name__ == "__main__":
    cards_by_commander = {}

    # Step 1: Scrape each commander URL for new cards
    for commander, url in COMMANDER_URLS.items():
        print(f"Scraping for {commander}...")
        cards = scrape_commander_cards(url)
        if cards:
            cards_by_commander[commander] = cards

    # Step 2: Filter out duplicates for each commander
    new_cards_by_commander = filter_new_cards(cards_by_commander)

    # Step 3: Send email if new cards are found for any commander
    if any(new_cards_by_commander.values()):
        print("Sending email with new card recommendations...")
    send_email(new_cards_by_commander)
    save_data(new_cards_by_commander)
else:
    print("No new planeswalkers to recommend for any commander.")

