from selenium_driver import driver
from selenium.webdriver.common.keys import Keys
from time import sleep
from data import email, password
ACC_TO_SEARCH = 'ironhackbcn'

class InstaFollower:
    def login(self):
        driver.get('https://www.instagram.com')
        driver.find_element_by_xpath('//button[text()="Accept"]').click()
        sleep(1)
        email_input = driver.find_element_by_name('username')
        email_input.send_keys(email)

        password_input = driver.find_element_by_name('password')
        password_input.send_keys(password)
        password_input.send_keys(Keys.ENTER)
        sleep(4)
        driver.find_element_by_xpath('//button[text()="Not Now"]').click()
        sleep(2)
        driver.find_element_by_xpath('//button[text()="Not Now"]').click()

    def find_followers(self):
        driver.find_element_by_xpath('//span[text()="Search"]').click()
        sleep(0.5)
        search_input = driver.find_element_by_xpath("//input[@placeholder='Search']")
        search_input.send_keys(ACC_TO_SEARCH)
        sleep(2)
        search_input.send_keys(Keys.DOWN)
        search_input.send_keys(Keys.ENTER)
        sleep(5)
