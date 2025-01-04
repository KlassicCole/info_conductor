# **EDH Commander Recommendation Scraper**
This project scrapes card recommendations for specified EDH (Elder Dragon Highlander) commanders from **EDHREC** and sends email notifications when new cards are suggested.

## **Features:**
- Scrapes multiple commanders from EDHREC for new card recommendations.
- Tracks previously recommended cards to avoid duplicate emails.
- Sends email notifications with grouped recommendations by commander.
- Lightweight and simple to run on a Raspberry Pi or any Python environment.

---

## **Requirements:**
- Python 3.8+
- SMTP Email Account (Gmail recommended)
- EDHREC URLs for desired commanders

---

## **Setup and Installation:**

### **1. Clone the Repository:**
```bash
git clone https://github.com/username/edh-oracle-scraper.git
cd edh-oracle-scraper
```

### **2. Create and Activate a Virtual Environment:**
```bash
python -m venv venv
source venv/bin/activate   # On Windows use venv\Scripts\activate
```

### **3. Install Required Packages:**
```bash
pip install -r requirements.txt
```

---

## **Configuration:**
Edit the `config.py` file to set up your email and SMTP server details:
```python
EMAIL = 'youremail@example.com'
PASSWORD = 'yourapppassword'
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
```

- If using Gmail, enable **App Passwords** or "Less Secure App Access."
- For other providers, adjust the SMTP settings accordingly.

---

## **How to Add Commanders:**
Open `main.py` and add or modify the commander URLs in the `COMMANDER_URLS` dictionary:
```python
COMMANDER_URLS = {
    'Atraxa, Praetors Voice': 'https://edhrec.com/commanders/atraxa-praetors-voice/planeswalkers',
    'Gargos Vicious Watcher': 'https://edhrec.com/commanders/gargos-vicious-watcher'
}
```

---

## **Running the Program:**
To start scraping and receive email notifications:
```bash
python src/main.py
```

- The program will scrape all specified commander URLs and email recommendations for new cards.
- **Duplicates are filtered** by saving previously recommended cards in `cards.json`.

---

## **Testing Email Functionality:**
To test the email feature directly:
```python
from emailer import send_email

test_data = {
    'Atraxa, Praetors Voice': [{'name': 'Teferi, Master of Time'}],
    'Krenko, Mob Boss': [{'name': 'Purphoros, God of the Forge'}]
}

send_email(test_data)
```

---

## **Troubleshooting:**
- **No Email Sent** – Check spam folders or confirm that new recommendations exist. If the scraper finds no new cards, the program finishes silently.
- **SMTP Errors** – Enable debugging by adding `server.set_debuglevel(1)` in `emailer.py`.

---

## **Future Improvements:**
- Automate daily scraping with cron jobs or Task Scheduler.
- Add Discord/Slack notifications.
- Scrape other sections like "Top Cards" or "Budget Cards."

---

## **Contributions:**
Contributions are welcome! Feel free to fork the repo and submit pull requests.  
