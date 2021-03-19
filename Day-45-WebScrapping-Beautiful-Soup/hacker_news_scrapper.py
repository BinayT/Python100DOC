from bs4 import BeautifulSoup
import requests

URL = 'https://news.ycombinator.com/'

ycombinator_data = requests.get(url=URL)

print(ycombinator_data.text)
