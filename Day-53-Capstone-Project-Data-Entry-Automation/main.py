from scrapper import ZillowScrapper

zillow_scrapper = ZillowScrapper()
zillow_scrapper.get_data()
for item in zillow_scrapper.links:
    print(item)
