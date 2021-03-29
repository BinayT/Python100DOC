from time import sleep
from selenium_driver import driver
SPEEDTEST_URL = 'https://www.speedtest.net/'


class SpeedTest:
    def __init__(self):
        self.start_running()
        self.download_speed = ''
        self.upload_speed = ''
        self.ping = ''
        self.distributor_name = ''

    def start_running(self):
        driver.get(SPEEDTEST_URL)
        driver.maximize_window()
        sleep(1)
        driver.find_element_by_id('_evidon-banner-acceptbutton').click()
        driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[1]/div/div/div/a').click()

    def get_internet_data(self):
        # This is running the program now
        driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')\
            .click()

        sleep(40)

        self.distributor_name = driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/'
                                                             'div[3]/div[3]/div/div[4]/div/div[2]/div/div[1]'
                                                             '/div/div[2]')
        self.ping = driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]'
                                                 '/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text

        self.download_speed = driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/'
                                                           'div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/'
                                                           'div/div[2]/span').text

        self.upload_speed = driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]'
                                                         '/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/'
                                                         'div[2]/span').text


hey = SpeedTest()
hey.get_internet_data()

