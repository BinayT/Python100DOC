from billboard_manager import BillboardManager
from spotify_manager import SpotifyManager

billboard_manager = BillboardManager()
top_100_songs_and_day = billboard_manager.scrape_top_100_songs()

spotify_manager = SpotifyManager(top_100_songs_and_day)
spotify_manager.search_songs()
