from selenium_driver import driver
from time import time, sleep

cookie_clicker_game_url = 'http://orteil.dashnet.org/experiments/cookie/'
driver.get(cookie_clicker_game_url)

initial_store = driver.find_elements_by_class_name('grayed')
cookie_object = driver.find_element_by_id('cookie')

initial_time = time()
while True:
    current_time = time()
    new_store = driver.find_elements_by_class_name('grayed')
    cookie_object.click()

    if current_time - initial_time > 5 and len(initial_store) != len(new_store):
        index_to_pick = (len(initial_store) - len(new_store))-1
        click_item = initial_store[index_to_pick].click()
        sleep(1)
        initial_time = current_time
        initial_store = new_store