# An adjacency matrix is a 2D matrix that shows the connections between nodes in a graph.
# The value at position (i,j) in the matrix is 1 if there is a connection between node i and node j, and 0 otherwise.
# In this case I'm working with directed graphs, but with undirected graphs the matrix would be symmetric.

from edges import edges

def create_graph_adjacency_matrix(n, edges):
  # Create a n x n matrix filled with zeros
  matrix = [[0 for _ in range(n)] for _ in range(n)]
    
  # Fill the matrix with the edges
  for edge in edges:
      matrix[edge[0]][edge[1]] = 1
    
  return matrix

def print_graph_adjacency_matrix(matrix):
  for row in matrix:
    print(row)

# Example
adjacency_matrix = create_graph_adjacency_matrix(6, edges)
print_graph_adjacency_matrix(adjacency_matrix)
