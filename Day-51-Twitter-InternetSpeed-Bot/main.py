from speedtest import SpeedTest
from selenium_driver import driver
from twitter import Twitter

speedtest = SpeedTest(driver)
speedtest.get_internet_data()
twitter = Twitter(driver)
