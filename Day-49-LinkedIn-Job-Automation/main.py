from selenium_driver import driver
from selenium.common.exceptions import NoSuchElementException
from time import sleep
url = 'https://www.linkedin.com'
email = '@gmail.com'
password = ''
job_title = 'React Developer'
job_location = 'Barcelona, Catalonia, Spain'

# Gets inside LinkedIn
driver.get(url)
sleep(0.5)

# Accepting cookies
driver.find_element_by_xpath('//*[@id="artdeco-global-alert-container"]/div[1]/section/div/div[2]/button[2]').click()
sleep(0.5)
# Clicks login button
click_login_button = driver.find_element_by_xpath('/html/body/nav/div/a[2]').click()

# Finds email and password input fields and it sends the respective
email_input = driver.find_element_by_id('username')
email_input.send_keys(email)

password_input = driver.find_element_by_id('password')
password_input.send_keys(password)

driver.find_element_by_xpath('//*[@id="organic-div"]/form/div[3]/button').click()
sleep(2)

driver.find_element_by_class_name('msg-overlay-bubble-header').click()
sleep(0.5)

driver.find_element_by_link_text('Jobs').click()
sleep(4)

job_title_input = driver.find_element_by_xpath("//input[starts-with(@id, 'jobs-search-box-keyword')]")
job_title_input.send_keys(job_title)

job_location_input = driver.find_element_by_xpath("//input[starts-with(@id, 'jobs-search-box-location')]")
job_location_input.send_keys(job_location)

driver.find_element_by_class_name('jobs-search-box__submit-button').click()
sleep(2)

driver.find_element_by_xpath('//button[text()="All filters"]').click()
sleep(1)

driver.find_element_by_xpath('//span[text()="Most recent"]').click()

driver.find_element_by_xpath('//span[text()="Show results"]').click()
sleep(2)
job_cards = driver.find_element_by_class_name('job-card-container').click()

apply_now = driver.find_element_by_xpath('//span[text()="Apply now"]').click()

try:
    submit_application = driver.find_element_by_xpath('//span[text()="Submit application"]')
except NoSuchElementException:
    driver.find_element_by_xpath('//button[@aria-label="Dismiss"]').click()
    sleep(1)
    driver.find_element_by_xpath('//span[text()="Discard"]').click()
else:
    driver.find_element_by_xpath('//label[contains(text()="Follow")]').click()
    submit_application.click()
