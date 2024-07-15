# An adjacency list is a simple way to represent a graph as a list of lists.
# Each element in the list is a list that contains the neighbors of a node.

from edges import edges

def create_graph_adjacency_list(n, edges):
  # Create a list of n empty lists
  adjacency_list = [[] for _ in range(n)]
    
  # Fill the adjacency list with the edges
  for edge in edges:
    adjacency_list[edge[0]].append(edge[1])
    
  return adjacency_list

def print_graph_adjacency_list(adjacency_list):
  for i, neighbors in enumerate(adjacency_list):
    print(f"Node {i} is connected to {neighbors}")

# Example
adjacency_list = create_graph_adjacency_list(6, edges)
print_graph_adjacency_list(adjacency_list)
