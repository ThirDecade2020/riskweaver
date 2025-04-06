import json
import os

# Define the JSON file that will store the country inquiry counts.
DATA_FILE = "country_inquiry_data.json"

def load_data():
    """
    Load the inquiry data from the JSON file.
    Returns a dictionary where keys are country names and values are inquiry counts.
    """
    if not os.path.exists(DATA_FILE):
        return {}
    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
    except json.JSONDecodeError:
        # If the file is empty or corrupted, start with an empty dictionary.
        data = {}
    return data

def save_data(data):
    """
    Save the inquiry data dictionary to the JSON file.
    """
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def record_country_inquiry(country_name):
    """
    Update the count for the given country.
    If the country doesn't exist, add it with a count of 1.
    """
    data = load_data()
    # Normalize the country name (strip extra spaces and convert to title case)
    normalized_country = country_name.strip().title()
    if normalized_country in data:
        data[normalized_country] += 1
    else:
        data[normalized_country] = 1
    save_data(data)

def get_country_inquiries():
    """
    Return the current dictionary of country inquiry counts.
    """
    return load_data()

