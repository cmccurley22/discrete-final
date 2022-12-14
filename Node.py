
class Node:
    #Initialize a Node
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        self.explored = False

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

    #Adds songs that difference makes them adjacent
    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()  

    #Get the ID of a particular Node
    def get_id(self):
        return self.id

    #returns the weight between two nodes
    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

    def set_explored(self):
        self.explored = True
