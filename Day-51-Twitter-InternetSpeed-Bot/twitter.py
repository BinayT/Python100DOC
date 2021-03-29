from data import email, password
from time import time, sleep
TWITTER_URL = 'https://www.twitter.com/'


class Twitter:
    def __init__(self, driver):
        self.driver = driver
        self.create_new_tab()
        self.enter_twitter()

    def create_new_tab(self):
        self.driver.execute_script('''window.open("https://www.twitter.com", "_blank");''')
        self.driver.switch_to.window(self.driver.window_handles[1])
        sleep(5)

    def enter_twitter(self):
        self.driver.find_element_by_xpath('//span[text()="Log in"]').click()
        sleep(1)
        email_field = self.driver.find_element_by_name('session[username_or_email]')
        email_field.send_keys(email)
        password_field = self.driver.find_element_by_name('session[password]')
        password_field.send_keys(password)
