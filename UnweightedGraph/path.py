'''
Breadth-first search traversal through an unweighted graph of the songs
to generate a path between two songs
'''

from graph import Node
import json

# read json file of data
with open("data2.json") as f:
    data = json.load(f)

# generate graph with songs as nodes
graph = [Node(i, data) for i in data]

# find the neighbors of each node (essentially, add edges to graph)
for node in graph:
    node.get_neighbors(graph, data)


def find_path(s1, s2):
    '''
    Using breadth-first search, traverse through the graph of song data to find
    paths between two songs

    Args:
        s1 (Node): the node for the starting song of the path
        s2 (Node): the node for the ending song of the path
    '''
    queue = []
    visited = []

    visited.append(s1)
    queue.append(s1)

    while s2 not in visited:
        # go through the queue of next possible nodes to visit
        while queue:
            m = queue.pop(0)

            # go through the neighbors of that node
            for neighbor in m.neighbors:
                if s2 in visited: return visited

                # check if we've already visited a node before queueing it
                if neighbor not in visited:
                    visited.append(neighbor)
                    queue.append(neighbor)


paths = find_path(graph[0], graph[1])
