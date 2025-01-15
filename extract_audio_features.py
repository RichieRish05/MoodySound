
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

song_uri = 'spotify:track:7qiZfU4dY1lWllzX7mPBI3'


CLIENT_ID = "5747a28aa2f0437fa06f3a9cb57ace03"
CLIENT_SECRET = "1a2133658b584d2aad3ce39786fba506"

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET))
track = spotify.track(song_uri, market='IT')


print('track    : ' + track['name'])
if track['preview_url']:
    print('audio    : ' + track['preview_url'])
print('cover art: ' + track['album']['images'][0]['url'])
print()