import requests
import json
import os
from secretkeys import user_name,password

# Function to convert city and state to latitude and longitude using geocoding
def get_coordinates(city, state):
    geocoding_api_url = f"https://nominatim.openstreetmap.org/search?city={city}&state={state}&format=json"
    response = requests.get(geocoding_api_url)
    if response.ok:
        data = response.json()
        # Extract latitude and longitude from the response
        if data:
            latitude = float(data[0]['lat'])
            longitude = float(data[0]['lon'])
            return latitude, longitude
        else:
            print("Geocoding API response empty")
    else:
        print("Failed to fetch data from Geocoding API")

# Function to fetch moon data based on city, state, and start date
def fetch_moon_data(city, state, start_date):
    latitude, longitude = get_coordinates(city, state)
    if latitude is not None and longitude is not None:
        # Construct API URLs
        api_urls = {
            "moon_set_api": f"https://api.meteomatics.com/{start_date}T00:00:00-04:00P30D:P1D/moonset:sql/{latitude},{longitude}/json",
            "moon_rise_api": f"https://api.meteomatics.com/{start_date}T00:00:00-04:00P30D:P1D/moonrise:sql/{latitude},{longitude}/json",
            "visible_moon_api": f"https://api.meteomatics.com/{start_date}T00:00:00ZP30D:P1D/moon_vis_area:p/{latitude},{longitude}/json"
        }


        for api_name, api_url in api_urls.items():
            response = requests.get(api_url, auth=(user_name, password))
            if response.ok:
                data = response.json()
                json_file_path = os.path.join('static', 'data', f'{api_name}.json')
                with open(json_file_path, "w") as json_file:
                    json.dump(data, json_file)
                print(f"Data from {api_name} API saved as JSON file: {json_file_path}")
            else:
                print(f"Failed to fetch data from {api_name} API. Status Code:", response.status_code)
                print("Response Content:", response.text)