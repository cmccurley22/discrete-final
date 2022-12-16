'''
Contains function for comparing any two songs
'''

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

    # calculate distances between song features of the two songs
    key_dist = abs(s1["key"] - s2["key"])
    tempo_dist = abs(s1["tempo"] - s2["tempo"])
    energy_dist = abs(s1["energy"] - s2["energy"])
    dance_dist = abs(s1["danceability"] - s2["danceability"])
    live_dist = abs(s1["liveness"] - s2["liveness"])
    acoustic_dist = abs(s1["acousticness"] - s2["acousticness"])

    # find how many common genres exist between the artists
    all_genres = s1["genre"] + s2["genre"]
    common_genres = len(all_genres) - len(set(all_genres))

    # calculate and return similarity index
    val = (key_dist / 11 + tempo_dist / 141.873 + energy_dist / .851 \
        + dance_dist / .76 + live_dist / .8922 + acoustic_dist / .955)
    return val / (common_genres + 1)
