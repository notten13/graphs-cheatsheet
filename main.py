from edge_list import EdgeList
from adjacency_matrix import AdjacencyMatrix
from adjacency_list import AdjacencyList

nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']

edges = [
  ('A', 'B'),
  ('A', 'D'),
  ('B', 'C'),
  ('C', 'H'),
  ('C', 'G'),
  ('D', 'E'),
  ('E', 'F'),
  ('H', 'I'),
  ('J', 'G'),
  ('J', 'K'),
  ('K', 'L'),
  ('K', 'M')
]

edge_list = EdgeList()
for edge in edges:
  edge_list.add_edge(edge)
print('Edge list:')
print(edge_list)

adjacency_matrix = AdjacencyMatrix(nodes)
for edge in edges:
  adjacency_matrix.add_edge(edge)
print('Adjacency matrix:')
print(adjacency_matrix)

adjacency_list = AdjacencyList(nodes)
for edge in edges:
  adjacency_list.add_edge(edge)
print('\nAdjacency list:')
print(adjacency_list)

print('DFS with edge list:')
edge_list.dfs('A', None)

print('DFS with adjacency list:')
adjacency_list.dfs('A', None)

print('DFS with adjacency matrix:')
adjacency_matrix.dfs('A', None)