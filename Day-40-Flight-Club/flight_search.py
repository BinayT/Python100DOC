import requests
from pprint import pprint
from keys_endpoints import TEQUILA_ENDPOINT, TEQUILA_HEADERS


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    def get_iata_codes(self, city_name):
            params = {
                "term": city_name,
            }
            tequila_locations_data = requests.get(url=f'{TEQUILA_ENDPOINT}/locations/query', headers=TEQUILA_HEADERS,
                                                  params=params).json()
            return tequila_locations_data['locations'][0]['code']
