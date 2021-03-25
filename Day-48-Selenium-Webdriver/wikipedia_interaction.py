from selenium_driver import driver
from selenium.webdriver.common.keys import Keys

wikipedia_mainpage_url = 'https://en.wikipedia.org/wiki/Main_Page'
app_brewery_newsletter = 'http://secure-retreat-92358.herokuapp.com/'

# driver.get(wikipedia_mainpage_url)

# articles_in_eng = driver.find_element_by_css_selector('#articlecount a:first-child')
# articles_in_eng.click()

# search_input = driver.find_element_by_name('search')
# search_input.send_keys('JavaScript')
# search_input.send_keys(Keys.ENTER)


driver.get(app_brewery_newsletter)

first_name = driver.find_element_by_name('fName')
first_name.send_keys('Binay')
last_name = driver.find_element_by_name('lName')
last_name.send_keys('Python Dev ;)')
email = driver.find_element_by_name('email')
email.send_keys('binay@python.py')
email.send_keys(Keys.ENTER)

# driver.close()