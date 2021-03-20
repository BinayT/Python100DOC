from bs4 import BeautifulSoup
import requests

URL = 'https://news.ycombinator.com/'

ycombinator_data = requests.get(url=URL).text

ycombinator_soup = BeautifulSoup(ycombinator_data, 'html.parser')
storylink_class = ycombinator_soup.find(name="a", class_='storylink') # Getting a tag with classname of storylink
storylink_class_text = storylink_class.getText() # Getting the text wrapped inside the a tag
storylink_class_href_link = storylink_class.get("href") # Getting the value of href of the a tage
print(storylink_class_href_link)

article_upvote = ycombinator_soup.find(name='span', class_="score") # Getting a span tag with classname score
article_upvote_number = article_upvote.getText().split(' ')[0] # Getting its text, splitting it and getting first el.
print(article_upvote_number)
