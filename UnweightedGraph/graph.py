'''
Data structure for a node in the unweighted graph
'''

from CompareSongs import compare_songs



class Node:
    """
    A class to represent a node in the graph, which is a song.

    Attributes:
    song : dict
        data about the song pulled from spotify
    
    neighbors : list
        a list of the nodes this graph is connected to, representing
        the four closest songs to it based on our similarity index

    Methods:
    get_neighbors(graph, song_data):
        finds the four closest nodes based on similarity index and
        connects them to this node

    """
    def __init__(self, song):
        self.song = song

    def get_neighbors(self, graph, song_data):
        closeness = [compare_songs(self.song, s) for s in song_data]

        min_vals = sorted(closeness)[1:5]

        close_songs = [graph[closeness.index(v)] for v in min_vals]

        self.neighbors = close_songs

