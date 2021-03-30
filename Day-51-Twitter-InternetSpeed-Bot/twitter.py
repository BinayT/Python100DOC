from data import email, password
from time import sleep
from datetime import datetime
TWITTER_URL = 'https://www.twitter.com/'
current_date_time = datetime.now().strftime("%B %d, %Y at %H:%M:%S")


class Twitter:
    def __init__(self, driver):
        self.driver = driver
        self.create_new_tab()
        self.enter_twitter()

    def create_new_tab(self):
        self.driver.execute_script('''window.open("https://www.twitter.com", "_blank");''')
        self.driver.switch_to.window(self.driver.window_handles[1])
        sleep(5)

    def click_login(self):
        self.driver.find_element_by_xpath('//span[text()="Log in"]').click()

    def enter_twitter(self):
        self.click_login()
        sleep(1)
        email_field = self.driver.find_element_by_name('session[username_or_email]')
        email_field.send_keys(email)
        password_field = self.driver.find_element_by_name('session[password]')
        password_field.send_keys(password)
        self.click_login()
        sleep(2)
        self.driver.find_element_by_xpath('//span[text()="Close"]').click()

    def write_speed(self, data):
        write_internet_speed = self.driver.find_element_by_class_name('public-DraftStyleDefault-block')
        write_internet_speed.send_keys(f"{current_date_time}\nThe internet's speed is\nPing:{data['ping']}\nDownload Speed"
                                       f": {data['download_speed']}\nUpload Speed: {data['upload_speed']}")
        self.driver.find_element_by_xpath('//span[text()="Tweet"]').click()