import requests
SHEETY_ENDPOINT = "https://api.sheety.co/28b51b82d298a761f7348503bed09834/flightDeals/prices"
HEADERS = {
    "Authorization": "Basic =="
}


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def get_data(self):
        cities = requests.get(url=SHEETY_ENDPOINT, headers=HEADERS).json()['prices']
        cities_names = [city['city'] for city in cities]
        return cities_names
