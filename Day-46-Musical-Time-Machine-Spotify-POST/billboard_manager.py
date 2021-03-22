from bs4 import BeautifulSoup as BS
import requests
BILLBOARD_SITE = 'https://www.billboard.com/charts/hot-100/2010-03-06'


class BillboardManager:
    def scrape_top_100_songs(self):
        billboard_data = requests.get(url=BILLBOARD_SITE).text

        billboard_soup = BS(billboard_data, 'html.parser')
        hot100_of_day = billboard_soup.find(name="button", class_='button--link').getText()\
            .replace('\n', '').strip()

        song_name = billboard_soup.find_all(name="span", class_="color--primary")
        song_name_list = [song.getText() for song in song_name]
        data = [hot100_of_day, song_name_list]
        return data
