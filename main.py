from SongGraph import SongGraph
import json

with open("edgesWeighted.json") as f:
    edges_data = json.load(f)

with open("data2.json") as f:
    data = json.load(f)

SG = SongGraph()
SG.add_vertex(data)
SG.add_edge(edges_data)

# As It Was --> I Don't Think That I Like Her
SG.dijkstra("As It Was","drivers license")
