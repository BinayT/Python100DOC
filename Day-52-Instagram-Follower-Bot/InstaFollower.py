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

        driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a').click()
        sleep(3)

    def follow(self):
        while True:
            follow = driver.find_elements_by_css_selector('.PZuss button')
            followed_amount = 0

            while followed_amount < 7:
                for i in range(len(follow)):
                    if follow[i].text != 'Follow':
                        follow[i].click()
                        sleep(2)
                        unfollow_button = driver.find_elements_by_css_selector('.mt3GC button')
                        unfollow_button[0].click()
                        sleep(2)

                    if follow[i].text == 'Follow':
                        follow[i].click()
                        sleep(3)

                    followed_amount += 1

            following_list = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
            driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", following_list)
            sleep(2)

