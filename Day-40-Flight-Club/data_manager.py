import requests
from keys_endpoints import SHEETY_ENDPOINT, SHEETY_AUTHORIZATION


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.google_sheet_data = {}

    def get_datas_from_sheety(self):
        self.google_sheet_data = requests.get(url=SHEETY_ENDPOINT, headers=SHEETY_AUTHORIZATION).json()['prices']

    # def update_iata_codes(self):
