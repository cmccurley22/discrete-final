import json

# read json file of data
with open("data2.json") as f:
    data = json.load(f)


def compare_songs(s1, s2):
    '''
    Compare two songs based on their keys, tempos, and energy levels
    read from the Spotify API

    Args:
        s1 (dict): track data for first song to compare
        s2 (dict): track data for second song to compare

    Returns
        float: a similarity value (out of 3) that is a sum of the similarity
            values (out of 1) of the three factors we're considering

    '''

    key_dist = abs(s1["key"] - s2["key"])
    tempo_dist = abs(s1["tempo"] - s2["tempo"])
    energy_dist = abs(s1["energy"] - s2["energy"])
    dance_dist = abs(s1["danceability"] - s2["danceability"])
    live_dist = abs(s1["liveness"] - s2["liveness"])
    acoustic_dist = abs(s1["acousticness"] - s2["acousticness"])

    '''print("Song 1")
    print("Key: " + str(s1["key"]))
    print("Tempo: " + str(s1["tempo"]))
    print("Energy: " + str(s1["energy"]))
    print("Artist Genres: " + str(s1["genre"]))

    print("Song 2")
    print("Key: " + str(s2["key"]))
    print("Tempo: " + str(s2["tempo"]))
    print("Energy: " + str(s2["energy"]))
    print("Artist Genres: " + str(s2["genre"]))'''


    all_genres = s1["genre"] + s2["genre"]
    common_genres = len(all_genres) - len(set(all_genres))

    val = (key_dist / 22 + tempo_dist / 141.873 + energy_dist / .851 \
        + dance_dist / .76 + live_dist / .8922 + acoustic_dist / .955)
    return val / common_genres if common_genres > 0 else val

