from bs4 import BeautifulSoup
import requests
import copy

URL = 'https://news.ycombinator.com/'

ycombinator_data = requests.get(url=URL).text

ycombinator_soup = BeautifulSoup(ycombinator_data, 'html.parser')

# Getting anchor tag with classname of storylink
storylink_class = ycombinator_soup.find_all(name="a", class_='storylink')
# Getting the list of titles of the article wrapped inside the anchor tag.
storylink_class_titles = [story.getText()for story in storylink_class]
# Getting the list of links from the anchor tags.
storylink_class_links = [story.get("href") for story in storylink_class]

# Getting a span tag with classname score
article_upvote = ycombinator_soup.find_all(name='span', class_="score")
# Getting its text, splitting it and getting first element.
article_upvote_numbers = [int(upvote.getText().split()[0])for upvote in article_upvote]

# Deep copying the upvotes numbers and sorting them in descending order.
article_upvote_descending_order = copy.deepcopy(article_upvote_numbers)
article_upvote_descending_order.sort(reverse=True)

votes_w_title_link = []
for votes in article_upvote_descending_order:
    index_of_title_link = article_upvote_numbers.index(votes)
    news_to_append = {
            "totalVotes": votes,
            "title": storylink_class_titles[index_of_title_link],
            "link": storylink_class_links[index_of_title_link]
    }
    votes_w_title_link.append(news_to_append)

print(votes_w_title_link)


