from bs4 import BeautifulSoup
import requests

URL = 'https://news.ycombinator.com/'

ycombinator_data = requests.get(url=URL).text

ycombinator_soup = BeautifulSoup(ycombinator_data, 'html.parser')
storylink_class = ycombinator_soup.find(name="a", class_='storylink')
storylink_class_text = storylink_class.getText()

article_upvote = ycombinator_soup.find(name='span', class_="score")
article_upvote_number = article_upvote.getText().split(' ')[0]
print(article_upvote_number)

article_link = ycombinator_soup.find(name="span", class_="sitestr").getText()
print(article_link)
