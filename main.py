import requests
from constants import API_KEY
import csv

# API Url
URL = 'https://clientculture.net/api/quarterly_results'

# Make requests

headers = {
    'x-api-secret': API_KEY,
}

response = requests.get(URL, headers=headers)

if response.status_code == 200:
    data = response.json()


    keys = data[0].keys()
    csv_filename = 'output.csv'

    with open(csv_filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=keys)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

    print(f"CSV file '{csv_filename}' created successfully.")
else:
    print(f"Failed to call API. Status code: {response.status_code}")
    print(response.text)

# print(content)
