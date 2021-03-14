import requests
from pprint import pprint
from tequila_data import HEADERS, TEQUILA_ENDPOINT


class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, data):
        self.data = data

    def hit_endpoint(self, params):
        return requests.get(url=TEQUILA_ENDPOINT, headers=HEADERS, params=params).json()

    def search_flights(self):
        for city in self.data:
            params = {
                "fly_from": "BCN",
                "fly_to": city['iataCode'],
                "date_from": "15/03/2021",
                "date_to": "15/09/2021",
                "flight_type": "round",
                "nights_in_dst_from": 7,
                "nights_in_dst_to": 28
            }

            search_data = self.hit_endpoint(params)['data']

            for flights in search_data:
                user_lowest_price = city['lowestPrice']
                data_lowest_price = flights['price']
                city_from = flights['cityFrom']
                city_to = flights['cityTo']
                departure_local = flights['route'][0]['local_departure'][:10]
                return_local = flights['route'][-1]['local_arrival'][:10]

                if data_lowest_price <= user_lowest_price:
                    print(f'{city_from} -- {city_to}, {departure_local} -- {return_local}'
                          f'-- Price: {data_lowest_price} euro')
                    break
