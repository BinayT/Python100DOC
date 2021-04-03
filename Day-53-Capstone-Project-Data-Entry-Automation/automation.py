from selenium_driver import driver
from selenium.webdriver.common.keys import Keys
from time import sleep
DOCS_LINK = 'https://forms.gle/sSHoDjGkSb9UgnAj6'


class AutomationDocs:
    def send_form(self, address, price, link):
        driver.get(DOCS_LINK)
        driver.maximize_window()
        sleep(2)
        address_input = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div'
                                                     '[1]/div/div[1]/input')
        price_input = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div'
                                                   '[1]/div/div[1]/input')
        link_input = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]'
                                                  '/div/div[1]/input')
        send_button = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span')

        address_input.send_keys(address)
        price_input.send_keys(price)
        link_input.send_keys(link)
        send_button.click()
        sleep(2)
        driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
        driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)
        driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')
