# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.
# -*- coding: utf-8 -*-
from data_manager import DataManager
from flight_search import FlightSearch

cities = ['Paris', 'Berlin', 'Tokyo', 'Sydney', 'Istanbul', 'Kuala Lumpur', 'New York', 'San Francisco', 'Cape Town',
          'Kathmandu']

# Initializing FlightSearch class and passing cities list as argument.
flight_search = FlightSearch(cities)
# # This function is responsible for search the IATA code for each city
cities_codes = flight_search.search_iata_of_cities()
# print(cities_codes)

# Initializing Sheety class
sheety_data_manager = DataManager()

# This posts respective IATA code to the City in our Google Sheets.
# sheety_data_manager.post_data(cities_codes)