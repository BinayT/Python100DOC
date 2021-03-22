from pprint import pprint
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIFY_ENDPOINT = 'https://api.spotify.com/'
# We can get all this from the spotify account and developer dashboard.
client_id = 'CLIENT ID HERE'
client_secret = 'CLIENT SECRET HERE'
scope = 'playlist-modify-private'
redirect_uri = 'http://example.com'
username ="USER ID HERE"
# cache_path === Name to be given to the .txt file
cache_path = 'token'
play_list_id = None


class SpotifyManager:
    def __init__(self, top_100_songs_and_day):
        # The top_100_songs_and_day is passed from billboard manager, which is a list with name and song list.
        self.top_100_songs = top_100_songs_and_day[1]
        self.day = top_100_songs_and_day[0]

        # This is the way we can auth using spotipy package for spotify
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            scope='playlist-modify-public', client_id=client_id,
            username=username, client_secret=client_secret, redirect_uri=redirect_uri, cache_path=cache_path))

    def search_songs(self):
        global play_list_id
        user_id = self.sp.me()['id']
        play_list = self.sp.user_playlist_create(user=user_id, name=f'Day of {self.day}',
                                                 description=self.day)
        play_list_id = play_list['id']

        tracks_to_add = []
        for song in self.top_100_songs:
            # Here we are trying to get track's uri, if there is no track, then it will simply pass to the next.
            try:
                search_songs = self.sp.search(q=song, type='track')
                track_uri = search_songs['tracks']['items'][0]['uri']
            except IndexError:
                pass
            else:
                # If there is no problem, then we append track's uri to the list.
                tracks_to_add.append(track_uri)

        # Then we finally add tracks in our playlist, items paramater is of type list.
        self.sp.playlist_add_items(playlist_id=play_list_id, items=tracks_to_add)
