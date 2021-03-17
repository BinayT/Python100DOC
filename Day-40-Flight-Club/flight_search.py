import requests
from pprint import pprint
from keys_endpoints import TEQUILA_ENDPOINT, TEQUILA_HEADERS
from flight_data import FlightData


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    def get_iata_codes(self, city_name):
        params = {
            "term": city_name,
        }
        tequila_locations_data = requests.get(url=f'{TEQUILA_ENDPOINT}/locations/query', headers=TEQUILA_HEADERS,
                                              params=params).json()
        return tequila_locations_data['locations'][0]['code']

    def check_flights(self, from_city, to_city, from_date, to_date):
        params= {
            'fly_from': from_city,
            'fly_to': to_city,
            'date_from': from_date.strftime("%d/%m/%Y"),
            'date_to': to_date.strftime("%d/%m/%Y"),
            'nights_in_dst_from': 7,
            'nights_in_dst_to': 28,
            "max_stopovers":0
        }

        response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search", headers=TEQUILA_HEADERS, params=params).json()

        try:
            data = response['data'][0]
        except IndexError:
            print(f'No flights for {from_city} -- {to_city}')
            return None
        else:
            flight_data = FlightData(
                price=data['price'],
                origin_city=data['route'][0]['cityFrom'],
                destination_city=data['route'][0]['cityTo'],
                origin_airport=data['route'][0]['flyFrom'],
                destination_airport=data['route'][0]['flyTo'],
                flight_date=data['route'][0]['local_departure'].split("T")[0],
                return_date=data['route'][1]['local_departure'].split("T")[0],
            )
            return flight_data


