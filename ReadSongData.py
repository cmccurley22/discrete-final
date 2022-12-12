import json

# read json file of data
with open("data.json") as f:
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

    all_genres = s1["genre"] + s2["genre"]
    common_genres = len(all_genres) - len(set(all_genres))

    return (key_dist / 11 + tempo_dist / 141.873 + energy_dist / .851)

