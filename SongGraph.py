from itertools import combinations
import networkx as nx
from Node import Node
import sys
import json

with open("artists.json") as f:
    artists = json.load(f)

class SongGraph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, data):
        for song in data:
            x = song["name"]
            self.num_vertices = self.num_vertices + 1
            new_vertex = Node(x)
            self.vert_dict[x] = new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, data):
        for x in range(len(data)):
            y = list(data[x].keys())
            key = y[0]
            edge_group = data[x][key]
            for i in range(4):
                self.vert_dict[key].add_neighbor(edge_group[i][1],edge_group[i][0])
                self.vert_dict[edge_group[i][1]].add_neighbor(key, edge_group[i][0])

    def get_vertices(self):
        return self.vert_dict.keys()

    def dijkstra(self, start_vertex, end_vertex):
      unexplored_vertices = list(self.get_vertices()) # List [unexplored vertex IDs]
      # Ex: ['1', '2', '3', '4', '5']

      shortest_dist = {} # Dict - {vertex ID : dist from source}
      previous_vertices = {} # Dict - {vertex ID : previous vertex ID}

      # Set all distances to maximum value
      for vertex in unexplored_vertices:
        shortest_dist[vertex] = sys.maxsize

      # Distance from start vertex to start vertex is 0
      # Set the start vertex as the current_min_vertex
      shortest_dist[start_vertex] = 0
      current_min_vertex = start_vertex

      # While the destination is not explored
      while end_vertex in unexplored_vertices:

        # Creates a dictionary of all unexplored vertcies and distances from source
        unexplored_weights = {} # Dict -- {unexplored vertex ID : dist from source}
        for vertex in unexplored_vertices:
          unexplored_weights[vertex] = shortest_dist[vertex]

        # Finds the least-valued unexplored vertex
        temp = min(unexplored_weights.values())
        current_min_vertex = [key for key in unexplored_weights if unexplored_weights[key] == temp]
        
        # Set the current vertex to explored and remove from unexplored_vertices
        unexplored_vertices.remove(current_min_vertex[0])
        
        unexplored_neighbors = self.get_vertex(current_min_vertex[0]).get_connections() # [vertex obj, vertex, obj, etc]

        for neighbor in unexplored_neighbors:
          # tentative value: estimated distance from neighbor to source vertex
          estimate_dist = shortest_dist[current_min_vertex[0]] + self.get_vertex(current_min_vertex[0]).get_weight(neighbor)

          # If the estimated distance from the neighbor to source vertex is
          # less than the current estimated distance from neighbor to source vertex
          if estimate_dist < shortest_dist[neighbor]:
            shortest_dist[neighbor] = estimate_dist # Update the new estimated distance
            previous_vertices[neighbor] = current_min_vertex[0] # Set the current min vertex as the previous vertex for the neighbor


      # Recreates the path by going through the previous_vertex list
      path_vertex = end_vertex
      shortest_path = [end_vertex]
      while path_vertex != start_vertex:
        shortest_path.append(previous_vertices[path_vertex])
        path_vertex = previous_vertices[path_vertex]
      shortest_path.reverse()
      
      # Prints the final shortest path
      for song in shortest_path:
        for artist in artists:
          if song in artist:
            print(song + " by " + artist[song])