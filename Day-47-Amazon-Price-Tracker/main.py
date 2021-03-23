from amazon_scrapper import AmazonScrapper
product_url = None



amazon_scrapper = AmazonScrapper()
data = amazon_scrapper.get_product_price()
print(data)
