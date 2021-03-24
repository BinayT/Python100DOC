from selenium_driver import driver
from pprint import pprint

python_org_url = 'https://www.python.org/'
driver.get(python_org_url)
list_elements = driver.find_elements_by_css_selector('.blog-widget ul.menu li')

list_of_events = {}
for index, val in enumerate(list_elements):
    date = val.find_element_by_css_selector('time')
    title = val.find_elements_by_css_selector('a')
    list_of_events[index] = {
        'time': date.text,
        'name': title[0].text
    }

pprint(list_of_events)

driver.close()
