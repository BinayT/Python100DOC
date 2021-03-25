from selenium_driver import driver

wikipedia_mainpage_url = 'https://en.wikipedia.org/wiki/Main_Page'

driver.get(wikipedia_mainpage_url)

articles_in_eng = driver.find_element_by_css_selector('#articlecount a:first-child')
print(articles_in_eng.text)

driver.close()