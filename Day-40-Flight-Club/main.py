from data_manager import DataManager
from flight_search import FlightSearch

sheety_data_manager = DataManager()
sheety_data = sheety_data_manager.get_datas_from_sheety()

flight_search = FlightSearch()

if sheety_data[0]['iataCode'] == '':
    for city in sheety_data:
        iata_code = flight_search.get_iata_codes(city['city'])
        city['iataCode'] = iata_code
    sheety_data_manager.update_iata_codes()
