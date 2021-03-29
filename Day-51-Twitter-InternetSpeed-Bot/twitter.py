from data import email, password
from time import time, sleep
TWITTER_URL = 'https://www.twitter.com/'

class Twitter:
    def __init__(self, driver):
        self.driver = driver
        self.create_new_tab()

    def create_new_tab(self):
        self.driver.execute_script('''window.open("https://www.twitter.com", "_blank");''')
        sleep(5)
