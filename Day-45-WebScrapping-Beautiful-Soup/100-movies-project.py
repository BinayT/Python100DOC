from bs4 import BeautifulSoup

with open('100_best_movies.html', mode='r', encoding="utf-8") as file:
    site_content = file.read()

soup = BeautifulSoup(site_content, 'html.parser')

titles = soup.find_all(name="h3", class_="jsx-2692754980")
titles_names = [title.getText() for title in titles]
titles_names.reverse()

with open('top-100-movies.txt', mode="w") as file:
    for movie in titles_names:
        file.write(f'{movie}\n')