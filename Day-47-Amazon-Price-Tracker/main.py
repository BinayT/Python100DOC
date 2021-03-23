from amazon_scrapper import AmazonScrapper
product_url = None

amazon_scrapper = AmazonScrapper()
data = amazon_scrapper.get_product_price()

if data:
    from email_manager import EmailManager
    email_manager = EmailManager(data)
    email_manager.send_message()
