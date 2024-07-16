# Depth-first search (DFS) means we traverse the graph by going as deep as possible until we reach a leaf

from edge_list import edges, nodes
from adjacency_list import create_graph_adjacency_list, print_graph_adjacency_list

def dfs(graph, start_node, visited):
  if start_node not in visited:
    print(start_node)
    visited.add(start_node)
    for neighbour in graph[start_node]:
      if neighbour not in visited:
        dfs(graph, neighbour, visited)

adjacency_list = create_graph_adjacency_list(nodes, edges)
print_graph_adjacency_list(adjacency_list)
visited = set()
dfs(adjacency_list, 'A', visited)
