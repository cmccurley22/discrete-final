"""""
Create a json file of all of the edges in our song graph
"""""

from ReadSongData import compare_songs
import json

# Read json file of data
with open("data.json") as f:
    data = json.load(f)

edges_data = []

def edges():
    """
    Creates the content of the edges database

    Args:
        None.

    Returns:
        edges_data: A list containing dictionary values of songs and the 4 most
                    similar songs along with their weights
    """

    for song_1 in data:

        edge_weights = [] # Resets list for every song

        for song_2 in data:
            
            # A list of the form [weight, compared song] which compares a
            # source song to one other song
            # Ex: [0.12010692305591691, 'As It Was']
            weight_list = [compare_songs(song_1,song_2),song_2["name"]]
            
            # A complete list of comparing a source song to every song in the
            # data base
            edge_weights.append(weight_list)

            # Sorts the list from closest in similarty to farthest in
            # similarity
            edge_weights = sorted(edge_weights)
            
            # Saves a list the 4 most similar songs
            # Ex: [[0.07680591145870402, "I am not a woman, I'm a god"], [0.11246569864212885, "Creep Wit Me"],
            #     [0.12010692305591691, "good 4 u"], [0.14097780274909305, "Somebody I Fucked Once"]]
            similar_songs = edge_weights[1:5]
            
            # A dictionary of the form {source song, similar songs list}
            edges_dict = {}
            edges_dict[song_1["name"]] = (similar_songs)
        
        edges_data.append(edges_dict)
    
    return edges_data

# Write song data to json file
with open("edgesWeighted.json", "w") as outfile:
    json.dump(edges(), outfile)
