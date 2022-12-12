"""""
Create a json file of all of the edges in our song graph
"""""

from ReadSongData import compare_songs
import json

# read json file of data
with open("data.json") as f:
    data = json.load(f)

edges_data = []

def edges():
    """
    Create a csv file of all of the edges in our song graph

    Args:
        path: A string representing the path to the csv file

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
            weight_list = [compare_songs(song_1,song_2),song_2["URI"]]
            
            # A complete list of comparing a source song to every song in the
            # data base
            edge_weights.append(weight_list)

            # Sorts the list from closest in similarty to farthest in
            # similarity
            edge_weights = sorted(edge_weights)
            
            # Saves a list the 4 most similar songs
            similar_songs = edge_weights[1:5]
            
            # A dictionary of the form {source song, similar songs list}
            edges_dict = {}
            edges_dict[song_1["URI"]] = (similar_songs)
        
        edges_data.append(edges_dict)
    
    return edges_data

# Write song data to json file
with open("edges.json", "w") as outfile:
    json.dump(edges(), outfile)
