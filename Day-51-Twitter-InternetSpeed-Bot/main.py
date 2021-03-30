from speedtest import SpeedTest
from selenium_driver import driver
from twitter import Twitter

speedtest = SpeedTest(driver)
speedtest.get_internet_data()

data_for_twitter = {
    'ping': speedtest.ping,
    'upload_speed': speedtest.upload_speed,
    'download_speed': speedtest.download_speed
}

twitter = Twitter(driver)
twitter.write_speed(data_for_twitter)