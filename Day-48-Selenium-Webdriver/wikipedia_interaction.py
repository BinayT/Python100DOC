from selenium_driver import driver

wikipedia_mainpage_url = 'https://en.wikipedia.org/wiki/Main_Page'

driver.get(wikipedia_mainpage_url)

articles_in_eng = driver.find_element_by_css_selector('#articlecount a:first-child')
# articles_in_eng.click()

search_input = driver.find_element_by_name('search')
search_input.send_keys('JavaScript')
search = driver.find_element_by_name('go')
search.click()
# driver.close()