import requests
from tequila_data import HEADERS, TEQUILA_ENDPOINT


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self, cities_names):
        self.cities_names = cities_names

    def hit_endpoint(self, params):
        return requests.get(url=TEQUILA_ENDPOINT, headers=HEADERS, params=params).json()

    def search_iata_of_cities(self):
        city_and_code = []
        for city in self.cities_names:
            params = {
                "term": city,
                "locale": "en-US",
                "location_types": "city"
            }
            get_info_city = self.hit_endpoint(params)
            city_and_code.append(get_info_city['locations'][0]['code'])
        return city_and_code
