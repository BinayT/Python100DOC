
import requests
headers = {
    "apikey": 'f55nrT6EMhIjueox-LYN1hO6iXc1Js7C',
}
TEQUILA_ENDPOINT = 'https://tequila-api.kiwi.com/locations/query'


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self, cities_names):
        self.cities_names = cities_names
        # print(self.cities_names)

    def search_iata_of_cities(self):
        city_and_code = []
        for city in self.cities_names:
            params = {
                "term": city,
                "locale": "en-US",
                "location_types": "city"
            }
            get_info_city = requests.get(url=TEQUILA_ENDPOINT, headers=headers, params=params).json()
            city_and_code.append(get_info_city['locations'][0]['code'])
        return city_and_code
