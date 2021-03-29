from selenium_driver import driver
from time import sleep
from selenium.common.exceptions import ElementClickInterceptedException
url = 'https://www.tinder.com'
email = '@gmail.com'
password = ''


driver.get(url)
# Click accept cookies
sleep(1)
driver.find_element_by_xpath('//span[text()="I Accept"]').click()

# Click Login
sleep(1)
driver.find_element_by_xpath('//span[text()="Log in"]').click()

# Login with Facebook
sleep(1)
driver.find_element_by_xpath('//span[text()="Log in with Facebook"]').click()
sleep(1)

# We targetting the popup here by making the selenium switch to the second window.
# This is how it's done, we first make driver handle first window then switch to that window.
facebook_window = driver.window_handles[1]
driver.switch_to.window(facebook_window)

# We getting the email and pass id from them and sending our credentials
email_input = driver.find_element_by_id('email')
email_input.send_keys(email)

password_input = driver.find_element_by_id('pass')
password_input.send_keys(password)

driver.find_element_by_id('loginbutton').click()

# We going back to the main tinder app here
base_window = driver.window_handles[0]
driver.switch_to.window(base_window)
sleep(5)

# Accepting the conditions if appeared
allow_tinder_location = driver.find_element_by_xpath('//span[text()="Allow"]').click()
sleep(1)
reject_notifications = driver.find_element_by_xpath('//span[text()="Not interested"]').click()
sleep(4)

dislike = '//*[@id="t--771258051"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button'
like = '//*[@id="t--771258051"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button'

# Now we start swiping left to all.
while True:
    try:
        swipe_left = driver.find_element_by_xpath(dislike).click()
    except ElementClickInterceptedException:
        driver.find_element_by_xpath('//span[text()="Not interested"]').click()
    sleep(2)
