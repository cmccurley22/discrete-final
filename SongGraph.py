import json
from CompareSongs import compare_songs

# read json file of data
with open("data2.json") as f:
    data = json.load(f)

class Node:
    def __init__(self, song, song_data):
        self.song = song

        closeness = [compare_songs(song, s) for s in song_data]

        min_vals = sorted(closeness)[1:4]

        close_songs = [song_data[closeness.index(v)] for v in min_vals]
        self.close_songs = close_songs
        
        
    def get_neighbors(self, graph, song_data):
        closeness = [compare_songs(self.song, s) for s in song_data]

        min_vals = sorted(closeness)[1:4]

        close_songs = [graph[closeness.index(v)] for v in min_vals]

        self.neighbors = close_songs

graph = [Node(i, data) for i in data]

for node in graph:
    node.get_neighbors(graph, data)

queue = []

def find_path(visited, graph, s1, s2):
    print(s1.song["name"])
    print(s2.song["name"])
    
    visited.append(s1)
    queue.append(s1)

    while s2 not in visited:
        while queue:
                m = queue.pop(0)
                
                for neighbor in m.neighbors:
                    if s2 in visited: return visited
                    if neighbor not in visited:
                        visited.append(neighbor)
                        queue.append(neighbor)


paths = find_path([], graph, graph[0], graph[1])

print("\n")

for s in paths:
    print(s.song["name"])
