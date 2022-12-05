import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json

# authentication
with open("client_secrets.json") as f:
    data = json.load(f)
    cid = data["client_id"]
    secret = data["client_secret"]

client_cred_manager = SpotifyClientCredentials(client_id = cid, \
    client_secret = secret)

sp = spotipy.Spotify(client_credentials_manager = client_cred_manager)

playlist_url = "https://open.spotify.com/playlist/64QxysD2w5x5EMLgcoT7fa"
uri = playlist_url.split("/")[-1].split("?")[0]

'''song_data = {
    "name": [],
    "artist": [],
    "URI": [],
    "tempo": [],
    "genre": [],
    "energy": [],
    "key": []
}'''

song_data = []

i = 0

for o in range(5):
    for track in sp.playlist_tracks(uri, limit = 100, offset = o * 100)["items"]:
        song = {}
        # URI
        track_uri = track["track"]["uri"]
        song["URI"] = (track_uri)

        # track name
        track_name = track["track"]["name"]
        song["name"] = (track_name)

        # artist info
        artist_uri = track["track"]["artists"][0]["uri"]
        artist_info = sp.artist(artist_uri)

        artist_name = track["track"]["artists"][0]["name"]
        artist_genres = artist_info["genres"]

        song["artist"] = (artist_name)
        song["genre"] = (artist_genres)

        # audio features
        features = sp.audio_features(track_uri)[0]
        song["tempo"] = (features["tempo"])
        song["energy"] = (features["energy"])
        song["key"] = (features["key"])

        song_data.append(song)

        print(i)
        i += 1

with open("test.json", "w") as outfile:
    json.dump(song_data, outfile)