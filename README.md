# Info Conductor

Info Conductor is a Python-based program designed to gather, process, and send information in an organized manner. The project currently supports scraping data from multiple sources and notifying users through email.

## Features
- **Rocket Launch Tracker**: Retrieves details about upcoming rocket launches from RocketLaunch.Live and sends updates via email in an elegant format.
- **Magic: The Gathering EDHREC Scraper**: Scrapes card recommendations for commanders and analyzes data for EDH decks.
- **Email Notifications**: Sends automated email updates with formatted data, including plain text and HTML options.

## How It Works
1. Choose a data source to scrape from (e.g., RocketLaunch.Live or EDHREC).
2. The program fetches and processes the data.
3. Outputs the data to a JSON file and optionally sends email updates to keep you informed.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Info_Conductor.git
   cd Info_Conductor
   ```
2. Set up a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration
1. Update the `config.py` file with your email credentials and any API keys needed for the data sources.
2. Modify paths or settings in the `config.py` file if necessary.

## Usage
Run the main program:
```bash
python src/main.py
```
Follow the menu prompts to:
- Scrape data from supported sources.
- Save the data locally in JSON format.
- Send email notifications with the gathered information.

## Example Output
### Email Notification
The program sends emails with formatted details, such as:

#### Rocket Launch Details
- **Mission**: Starlink (12-7)
- **Date**: January 27, 2025, 8:22 PM UTC
- **Location**: Cape Canaveral SFS
- **Vehicle**: Falcon 9
- **Description**: A SpaceX Falcon 9 rocket will launch the Starlink mission.

## Contributions
Contributions are welcome! Feel free to fork the repository and submit a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
