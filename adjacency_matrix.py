# An adjacency matrix is a 2D matrix that shows the connections between nodes in a graph.
# The value at position (i,j) in the matrix is 1 if there is a connection between node i and node j, and 0 otherwise.
# In this case I'm working with directed graphs, but with undirected graphs the matrix would be symmetric.

class AdjacencyMatrix:
  def __init__(self, nodes):
    self.node_to_index = {node: index for index, node in enumerate(nodes)}
    self.matrix = [[0 for _ in nodes] for _ in nodes]
  
  def add_edge(self, edge):
    self.matrix[self.node_to_index[edge[0]]][self.node_to_index[edge[1]]] = 1

  def dfs(self, start_node, visited):
    if visited is None:
      visited = set()
    if start_node not in visited:
      print(start_node)
      visited.add(start_node)
      neighbours = self.matrix[self.node_to_index[start_node]]
      for index, neighbour in enumerate(neighbours):
        if neighbour == 1:
          neighbour_node = [node for node, i in self.node_to_index.items() if i == index][0]
          self.dfs(neighbour_node, visited)

  def __repr__(self):
    return '\n'.join([' '.join([str(cell) for cell in row]) for row in self.matrix])
