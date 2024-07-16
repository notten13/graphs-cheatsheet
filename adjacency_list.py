# An adjacency list is a simple way to represent a graph as a list of lists.
# Each element in the list is a list that contains the neighbors of a node.

class AdjacencyList:
  def __init__(self, nodes):
    self.graph = { key: [] for key in nodes }

  def add_edge(self, edge):
    self.graph[edge[0]].append(edge[1])

  def __repr__(self):
    return '\n'.join([f'{node}: {neighbours}' for node, neighbours in self.graph.items()])
    