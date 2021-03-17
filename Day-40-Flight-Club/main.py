from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from datetime import datetime, timedelta

ORIGIN_CITY = "BCN"

sheety_data_manager = DataManager()
sheety_data = sheety_data_manager.get_datas_from_sheety()

flight_search = FlightSearch()

if sheety_data[0]['iataCode'] == '':
    for city in sheety_data:
        iata_code = flight_search.get_iata_codes(city['city'])
        city['iataCode'] = iata_code
    sheety_data_manager.update_iata_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

sheety_data_manager.get_users_from_sheety()

# message = ''
# for city_data in sheety_data:
#     flights = flight_search.check_flights(
#         from_city=ORIGIN_CITY,
#         to_city=city_data['iataCode'],
#         from_date=tomorrow,
#         to_date=six_month_from_today
#     )
#     if flights is None:
#         continue
#     if flights.price < city_data['lowestPrice']:
#         message += f'Cheap Flight Alert...\nFrom {flights.origin_city}-{flights.origin_airport} ---> ' \
#                   f'{flights.destination_city}-{flights.destination_airport} just for {flights.price} EURO\n\n'
#
# if message != '':
#     NotificationManager().send_message(message)