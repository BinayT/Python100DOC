from speedtest import SpeedTest
from selenium_driver import driver
from twitter import Twitter

speedtest = SpeedTest(driver)
speedtest.get_internet_data()
twitter = Twitter(driver)


# driver.maximize_window()
# driver.get("https://www.cntraveller.in/")
# # to fire up a new tab using javascript and load google.com
# driver.execute_script('''window.open("https://www.google.com", "_blank");''')
# time.sleep(5)
# driver.quit()
