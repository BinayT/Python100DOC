import requests
SHEETY_ENDPOINT = "https://api.sheety.co/28b51b82d298a761f7348503bed09834/flightDeals/prices"
HEADERS = {
    "Authorization": "Basic =="
}


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.cities_w_id = requests.get(url=SHEETY_ENDPOINT, headers=HEADERS).json()['prices']

    def get_cities(self):
        cities_names = [city for city in self.cities_w_id]
        return cities_names

    def get_all_data(self):
        return self.cities_w_id


    def post_data(self, city_iata):
        for x in range(len(self.cities_w_id)):
            body = {
                "price": {
                    "iataCode": city_iata[x]
                }
            }
            city_code = requests.put(url=f"{SHEETY_ENDPOINT}/{self.cities_w_id[x]['id']}", headers=HEADERS, json=body)
            print(city_code.text)