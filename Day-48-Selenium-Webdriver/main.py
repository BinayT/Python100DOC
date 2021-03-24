from selenium import webdriver

# Path of the chromedriver
chromedriver_path = r'C:\Users\binay\OneDrive\Escritorio\Python\Chromedriver_win32\chromedriver.exe'

# We choose chrome and the path will be where the chromedriver is located
driver = webdriver.Chrome(executable_path=chromedriver_path)

driver.get('https://www.google.com')
