from datetime import datetime
def scrape_rocketlaunch():
    """
    Scrape rocket launch data from RocketLaunch.Live API.
    """
    import requests
    from config import ROCKETLAUNCH_FREE_URL

    try:
        response = requests.get(ROCKETLAUNCH_FREE_URL)
        response.raise_for_status()
        data = response.json()
        launches = []

        for launch in data.get("result", []):
            # Extract basic information
            name = launch.get("name", "No Mission Name")
            location = launch.get("pad", {}).get("location", {}).get("name", "Unknown Location")
            vehicle = launch.get("vehicle", {}).get("name", "Unknown Vehicle")

            # Extract date
            t0 = launch.get("t0")  # Exact launch time
            est_date = launch.get("est_date", {})  # Estimated date details
            date_str = None

            if t0:
                try:
                    # Parse and format exact launch time
                    t0_datetime = datetime.strptime(t0, "%Y-%m-%dT%H:%MZ")
                    date_str = t0_datetime.strftime("%B %d, %Y %I:%M %p UTC")
                except ValueError:
                    date_str = "Invalid Date Format"
            elif est_date.get("year"):
                # Handle estimated date
                year = est_date.get("year")
                month = est_date.get("month")
                day = est_date.get("day")

                if month and day:
                    date_str = f"{datetime(year, month, day).strftime('%B %d, %Y')}"
                elif month:
                    date_str = f"{datetime(year, month, 1).strftime('%B %Y')}"
                else:
                    date_str = f"{year}"
            else:
                date_str = "TBD"

            # Append the launch data
            launches.append({
                "mission": name,
                "vehicle": vehicle,
                "date": date_str,
                "location": location,
                "description": launch.get("launch_description", "No description available"),
            })

        return launches

    except Exception as e:
        print(f"Error fetching data from RocketLaunch.Live: {e}")
        return []


# Example usage:
if __name__ == "__main__":
    launches = scrape_rocketlaunch()
    if launches:
        for launch in launches:
            print(f"Mission: {launch['mission']}, Date: {launch['date']}, "
                  f"Location: {launch['location']}, Vehicle: {launch['vehicle']}, Provider: {launch['provider']}")
    else:
        print("No launches found.")