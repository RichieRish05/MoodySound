import requests

BASE_URL = "https://musicbrainz.org/ws/2"
def get_music_brainz_id(song_name, artist):
    search_url = BASE_URL + "/recording"
    print(search_url)
    search_url= "https://musicbrainz.org/ws/2/recording"
    params = {
        "query": f'track:"{song_name}" AND artist:"{artist}"',
        "fmt": "json"
    }

    #Make the get request
    response = requests.get(search_url, params=params)
    data = response.json()
    id = data["recordings"][0]["id"]

    return id