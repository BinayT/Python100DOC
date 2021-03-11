# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.
# -*- coding: utf-8 -*-
from data_manager import DataManager
from flight_search import FlightSearch

cities = ['Paris', 'Berlin', 'Tokyo', 'Sydney', 'Istanbul', 'Kuala Lumpur', 'New York', 'San Francisco', 'Cape Town',
          'Kathmandu']


sheety_data_manager = DataManager()

flight_search = FlightSearch(cities)
flight_search.post_IATA()