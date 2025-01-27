from data_sources.edhrec import scrape_commander_cards
from data_sources.rocketlaunch import scrape_rocketlaunch
# from emailers.edh_emailer import send_edhrec_email
from emailers.rocketlaunch_emailer import send_rocketlaunch_email
# from edh_tracker import filter_new_cards, save_data as save_edh_data, load_data as load_edh_data
from data.rocketlaunch_tracker import filter_new_launches, save_launch_data, load_launch_data

def main():
    while True:
        print("\n--- Info Conductor Menu ---")
        print("1. Scrape EDHREC")
        print("2. Scrape RocketLaunch.Live")
        print("3. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            edhrec_workflow()
        elif choice == "2":
            rocketlaunch_workflow()
        elif choice == "3":
            print("Exiting Info Conductor. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def edhrec_workflow():
    print("\nStarting EDHREC Workflow...")
    saved_data = load_edh_data()
    scraped_data = scrape_commander_cards()
    new_data = filter_new_cards(scraped_data)
    if new_data:
        send_edhrec_email(new_data)
        save_edh_data(new_data)
    else:
        print("No new EDHREC data to process.")

def rocketlaunch_workflow():
    print("\nStarting RocketLaunch.Live Workflow...")
    saved_data = load_launch_data()
    scraped_data = scrape_rocketlaunch()
    new_data = filter_new_launches(scraped_data)
    if new_data:
        print("New rocket launches found. Sending email...")
        send_rocketlaunch_email(new_data)
        save_launch_data(new_data)
    else:
        print("No new rocket launches to process.")

if __name__ == "__main__":
    main()