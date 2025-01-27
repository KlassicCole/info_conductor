import os
import json
from config import ROCKETLAUNCH_SAVE_PATH

def load_launch_data():
    """
    Load past rocket launch data from a JSON file.
    If the file doesn't exist, return an empty list.
    """
    try:
        with open(ROCKETLAUNCH_SAVE_PATH, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("No past launches file found. Starting fresh.")
        return []
    except json.JSONDecodeError:
        print("Error decoding past launches file. Starting fresh.")
        return []

def save_launch_data(launches):
    """
    Save rocket launch data to a JSON file.
    """
    try:
        # Ensure the directory for the save path exists
        os.makedirs(os.path.dirname(ROCKETLAUNCH_SAVE_PATH), exist_ok=True)

        # Write to the file
        with open(ROCKETLAUNCH_SAVE_PATH, "w") as file:
            json.dump(launches, file, indent=4)
        print(f"Saved {len(launches)} rocket launches to {ROCKETLAUNCH_SAVE_PATH}")
    except Exception as e:
        print(f"Error saving past launches: {e}")

def filter_new_launches(scraped_launches):
    """
    Compare scraped launches with past launches and filter out duplicates.
    Only return new launches that are not already in the past launches file.

    You may need to limit the amount it compares to your saved launches this data comparison could get long.
    """
    past_launches = load_launch_data()
    new_launches = []

    # Compare each scraped launch with past launches
    for launch in scraped_launches:
        if not any(
                past_launch["mission"] == launch["mission"] and
                past_launch["date"] == launch["date"]
                for past_launch in past_launches
        ):
            new_launches.append(launch)

    return new_launches

def update_launch_data(new_launches):
    """
    Append new launches to the past launches file.
    """
    past_launches = load_launch_data()
    updated_launches = past_launches + new_launches
    save_launch_data(updated_launches)

# Example usage (can be removed in production):
if __name__ == "__main__":
    # Mock data
    scraped_data = [
        {"mission": "Starlink-60", "date": "2025-01-30", "location": "Cape Canaveral"},
        {"mission": "Artemis I", "date": "2025-02-10", "location": "Kennedy Space Center"},
    ]

    new_launches = filter_new_launches(scraped_data)
    if new_launches:
        print("New launches found:")
        for launch in new_launches:
            print(launch)
        update_launch_data(new_launches)
    else:
        print("No new launches to add.")