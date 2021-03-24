from selenium import webdriver

# Path of the chromedriver
chromedriver_path = r'C:\Users\binay\OneDrive\Escritorio\Python\Chromedriver_win32\chromedriver.exe'

# We choose chrome and the path will be where the chromedriver is located
driver = webdriver.Chrome(executable_path=chromedriver_path)

# Now we get the google's page and if we run this code then a chrome tab appears with google page.
driver.get('https://www.google.com')
driver.close()
