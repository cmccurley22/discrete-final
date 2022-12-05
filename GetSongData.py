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

song_data = {
    "name": [],
    "artist": [],
    "URI": [],
    "tempo": [],
    "genre": [],
    "energy": [],
    "key": []
}

i = 0

for o in range(5):
    for track in sp.playlist_tracks(uri, limit = 100, offset = o * 100)["items"]:
        # URI
        track_uri = track["track"]["uri"]
        song_data["URI"].append(track_uri)

        # track name
        track_name = track["track"]["name"]
        song_data["name"].append(track_name)

        # artist info
        artist_uri = track["track"]["artists"][0]["uri"]
        artist_info = sp.artist(artist_uri)

        artist_name = track["track"]["artists"][0]["name"]
        artist_genres = artist_info["genres"]

        song_data["artist"].append(artist_name)
        song_data["genre"].append(artist_genres)

        # audio features
        features = sp.audio_features(track_uri)[0]
        song_data["tempo"].append(features["tempo"])
        song_data["energy"].append(features["energy"])
        song_data["key"].append(features["key"])

        print(i)
        i += 1

with open("test.json", "w") as outfile:
    json.dump(song_data, outfile)