import requests

API_KEY = ''


class MovieSearcher:
    def get_all_movies(self, movie_name):
        params = {
            'api_key': API_KEY,
            'language': 'en-US',
            'include_adult': 'false',
            'query': movie_name
        }
        movies = requests.get('https://api.themoviedb.org/3/search/movie', params=params).json()['results']
        return movies
