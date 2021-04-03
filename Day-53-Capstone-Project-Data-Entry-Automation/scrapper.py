from bs4 import BeautifulSoup
from requests import get
from time import sleep
LINK = 'https://www.zillow.com'
SITE_TO_OPEN = 'https://www.zillow.com/san-francisco-ca/rentals/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7' \
               'D%2C%22usersSearchTerm%22%3A%22San%20Francisco%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.644' \
               '81581640625%2C%22east%22%3A-122.22184218359375%2C%22south%22%3A37.64220115428586%2C%22north%22%3A37.90' \
               '8142595089735%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%' \
               '2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo' \
               '%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%' \
               '3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf' \
               '%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3' \
               'Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A' \
               '%7B%22max%22%3A894487%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22ma' \
               'pZoom%22%3A11%7D'
HEADERS = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1) AppleWebKit/605.1.15 (KHTML, like Gecko) "
                          "Version/14.0.2 Safari/605.1.15",
            "Accept-Language": "en-US"
        }


class ZillowScrapper:
    def __init__(self):
        self.prices = []
        self.links = []
        self.addresses = []

    def get_data(self):
        zillow_site = get(url=SITE_TO_OPEN, headers=HEADERS).text
        soup = BeautifulSoup(zillow_site, 'html.parser')
        prices_list = soup.find_all(name="div", class_='list-card-price')
        links_container = soup.find_all(name="div", class_='list-card-info')
        links_list = [item.find(name="a", class_="list-card-link") for item in links_container]
        addresses_list = soup.find_all(name="address", class_='list-card-addr')

        self.prices = [price.getText()[:6] for price in prices_list]
        self.links = [f"{LINK}{link['href']}" if link['href'].startswith('/') else link['href']
                      for link in links_list]
        self.addresses = [address.getText() for address in addresses_list]