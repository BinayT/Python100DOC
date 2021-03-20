from bs4 import BeautifulSoup
import requests

URL = 'https://news.ycombinator.com/'

ycombinator_data = requests.get(url=URL).text

ycombinator_soup = BeautifulSoup(ycombinator_data, 'html.parser')

# Getting a tag with classname of storylink
storylink_class = ycombinator_soup.find_all(name="a", class_='storylink')
# Getting the list of titles of the article wrapped inside the a tag.
storylink_class_texts = [story.getText()for story in storylink_class]
# Getting the list of links from the a tags.
storylink_class_href_links = [story.get("href") for story in storylink_class]

# Getting a span tag with classname score
article_upvote = ycombinator_soup.find(name='span', class_="score")
# Getting its text, splitting it and getting first element.
article_upvote_number = int(article_upvote.getText().split()[0])


