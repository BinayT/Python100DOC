from bs4 import BeautifulSoup as BS
import requests
BILLBOARD_SITE = 'https://www.billboard.com/charts/hot-100/2010-03-06'


class BillboardManager:
    def scrape_billboard(self):
        billboard_data = requests.get(url=BILLBOARD_SITE).text

        billboard_soup = BS(billboard_data, 'html.parser')
        song_name = billboard_soup.find_all(name="span", class_="color--primary")
        song_name_list = [song.getText() for song in song_name]
        return song_name_list
