import requests
from bs4 import BeautifulSoup
import json

url = "https://wiki.warthunder.com/List_of_vehicle_battle_ratings/Land"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

tanks_data = []

# Extracting relevant information from the HTML
for row in soup.find_all('tr')[1:]:
    columns = row.find_all('td')
    if len(columns) >= 4:
        tank_name = columns[2].text.strip()
        battle_rating = (columns[3].text.strip())
        nation = columns[0].text.strip()
        tank_type = columns[1].text.strip()

        tank_info = {
            "name": tank_name,
            "battle_rating": battle_rating,
            "nation": nation,
            "type": tank_type
        }

        tanks_data.append(tank_info)

# Creating a JSON file with the extracted data
output_file = "tanks_data.json"
with open(output_file, 'w') as json_file:
    json.dump({"tanks": tanks_data}, json_file, indent=2)

print(f"Scraped data saved to {output_file}")
