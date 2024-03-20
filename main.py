import requests
from constants import API_KEY, URL
import csv


# Create Header for the API request
HEADERS = {
    'x-api-secret': API_KEY,
}


# Make requests
response = requests.get(URL, headers=HEADERS)


if response.status_code == 200:
    # Date to .json
    data = response.json()

    # Get the keys from the response
    keys = data[0].keys()

    # Create the CSV
    csv_filename = 'ClientSense.csv'

    # Open the CSV file
    with open(csv_filename, 'w', newline='') as csvfile:
        # Write the data to a .csv file
        writer = csv.DictWriter(csvfile, fieldnames=keys)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

    # Error Handling
    print(f"CSV file '{csv_filename}' created successfully.")
else:
    print(f"Failed to call API. Status code: {response.status_code}")
    print(response.text)

# print(content)
