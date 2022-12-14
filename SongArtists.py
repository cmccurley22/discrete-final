"""""
Create a json file of all the songs with their corresponding artist
"""""

import json

# Read json file of data
with open("data2.json") as f:
    data = json.load(f)

song_artists = []

def artists():
    """
    Creates the content of the artists database

    Args:
        None.

    Returns:
        song_artists: A list containing dictionaries songs with their
                      corresponding artist
    """

    for song in data:

        # Creates a ditionary of form {song name : artist}
        song_artists.append({song["name"] : song["artist"]})
    
    return song_artists

# Write song data to json file
with open("artists.json", "w") as outfile:
    json.dump(artists(), outfile)