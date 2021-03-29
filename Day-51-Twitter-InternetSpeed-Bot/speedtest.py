from time import sleep
SPEEDTEST_URL = 'https://www.speedtest.net/'


class SpeedTest:
    def __init__(self, driver):
        self.driver = driver
        self.start_running()
        self.download_speed = ''
        self.upload_speed = ''
        self.ping = ''
        self.distributor_name = ''

    def start_running(self):
        self.driver.get(SPEEDTEST_URL)
        self.driver.maximize_window()
        sleep(1)
        self.driver.find_element_by_id('_evidon-banner-acceptbutton').click()
        self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[1]/div/div/div/a').click()

    def get_internet_data(self):
        # This is running the program now
        self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')\
            .click()

        sleep(40)

        self.distributor_name = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/'
                                                             'div[3]/div[3]/div/div[4]/div/div[2]/div/div[1]'
                                                             '/div/div[2]')
        self.ping = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]'
                                                 '/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text

        self.download_speed = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/'
                                                           'div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/'
                                                           'div/div[2]/span').text

        self.upload_speed = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]'
                                                         '/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/'
                                                         'div[2]/span').text
