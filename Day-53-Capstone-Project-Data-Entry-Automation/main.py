from scrapper import ZillowScrapper
from automation import AutomationDocs

zillow_scrapper = ZillowScrapper()
zillow_scrapper.get_data()

prices = zillow_scrapper.prices
links = zillow_scrapper.links
addresses = zillow_scrapper.addresses

docs_automation = AutomationDocs()

for i in range(len(prices)):
    docs_automation.send_form(addresses[i], prices[i], links[i])
