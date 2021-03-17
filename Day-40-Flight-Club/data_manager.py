import requests
from keys_endpoints import SHEETY_ENDPOINT, SHEETY_AUTHORIZATION


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.google_sheet_data = {}
        self.google_sheet_users = None

    def get_datas_from_sheety(self):
        self.google_sheet_data = requests.get(url=f'{SHEETY_ENDPOINT}/prices', headers=SHEETY_AUTHORIZATION).json()['prices']
        print(self.google_sheet_data)
        return self.google_sheet_data

    def update_iata_codes(self):
        for city in self.google_sheet_data:
            params = {
                'price': {
                    'iataCode': city['iataCode']
                }
            }
            res = requests.put(url=f'{SHEETY_ENDPOINT}/prices/{city["id"]}', json=params, headers=SHEETY_AUTHORIZATION)

    def get_users_from_sheety(self):
        self.google_sheet_users = requests.get(url=f'{SHEETY_ENDPOINT}/users',
                                               headers=SHEETY_AUTHORIZATION).json()['users']
        return self.google_sheet_users