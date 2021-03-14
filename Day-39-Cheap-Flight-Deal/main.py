# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.
# -*- coding: utf-8 -*-
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData

cities = ['Paris', 'Berlin', 'Tokyo', 'Sydney', 'Istanbul', 'Kuala Lumpur', 'New York', 'San Francisco', 'Cape Town',
          'Kathmandu']

# Initializing Sheety class
sheety_data_manager = DataManager()

# Getting all cities with their id and everything.
cities_all_datas = sheety_data_manager.get_all_data()

# Initializing FlightSearch class and passing cities list as argument.
flight_search = FlightSearch(cities)

# Initializing FlightData class and passing cities list as argument.
user_flight_data_search = FlightData(cities_all_datas)
user_flight_data_search.search_flights()

# # This function is responsible for search the IATA code for each city
# cities_codes = flight_search.search_iata_of_cities()





# This posts respective IATA code to the City in our Google Sheets.
# sheety_data_manager.post_data(cities_codes)