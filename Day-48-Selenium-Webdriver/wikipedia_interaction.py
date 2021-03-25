from selenium_driver import driver
from selenium.webdriver.common.keys import Keys

wikipedia_mainpage_url = 'https://en.wikipedia.org/wiki/Main_Page'

driver.get(wikipedia_mainpage_url)

articles_in_eng = driver.find_element_by_css_selector('#articlecount a:first-child')
# articles_in_eng.click()

search_input = driver.find_element_by_name('search')
search_input.send_keys('JavaScript')
search_input.send_keys(Keys.ENTER)
# driver.close()