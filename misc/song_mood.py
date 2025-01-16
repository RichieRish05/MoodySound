import requests


def get_music_brainz_id(song_name, artist):
    BASE_URL = "https://musicbrainz.org/ws/2"
    search_url = BASE_URL + "/recording"
    search_url= "https://musicbrainz.org/ws/2/recording"
    params = {
        "query": f'track:"{song_name}" AND artist:"{artist}"',
        "fmt": "json"
    }

    #Make the get request
    response = requests.get(search_url, params=params)
    data = response.json()

    
    if data["recordings"]:
        return data["recordings"][0]["id"]

    return None

def get_song_mood(song_id):
    BASE_URL = "https://acousticbrainz.org"
    search_url = BASE_URL + f"/{song_id}/high-level"
    response = requests.get(search_url)
    data = response.json()

    mood_features = [
        "danceability",
        "mood_acoustic",
        "mood_aggressive",
        "mood_electronic",
        "mood_happy",
        "mood_party",
        "mood_relaxed",
        "mood_sad",
        "timbre",
        "tonal_atonal",
        "voice_instrumental"
    ]

    if data.get("message"):
        return data
    mood_vector = {}
    
    for feature in mood_features:
        if feature in data["highlevel"]:
            mood_vector[feature] = data["highlevel"][feature]["probability"]

    return data



print(get_music_brainz_id("Titi me Pregunta", "Bad Bunny"))
print(get_song_mood(get_music_brainz_id("Organito de la Tarde", "Trio Hugo Diaz")))
