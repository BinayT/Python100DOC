from bs4 import BeautifulSoup as BS
import requests
# Here I'm getting the URL for the site and date to scrape
BILLBOARD_SITE = 'https://www.billboard.com/charts/hot-100/2010-03-06'


class BillboardManager:
    def scrape_top_100_songs(self):
        billboard_data = requests.get(url=BILLBOARD_SITE).text

        # Parsing the text from the request to html, and with that we can work with BS
        billboard_soup = BS(billboard_data, 'html.parser')

        # Getting the button that has class of button--link which contains the date
        hot100_of_day = billboard_soup.find(name="button", class_='button--link').getText()\
            .replace('\n', '').strip()

        # Finding all spans with class name of color--primary which contains the name of the song.
        song_name = billboard_soup.find_all(name="span", class_="color--primary")
        # Getting the text of the song and saving it in a list with list comprehension
        song_name_list = [song.getText() for song in song_name]
        data = [hot100_of_day, song_name_list]
        # Sending songs and date as return
        return data
