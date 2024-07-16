class EdgeList:
  def __init__(self):
    self.edges = []

  def add_edge(self, edge):
    self.edges.append(edge)

  def dfs(self, start_node, visited):
    if visited is None:
      visited = set()
    if start_node not in visited:
      print(start_node)
      for edge in self.edges:
        if edge[0] == start_node and edge[1] not in visited:
          self.dfs(edge[1], visited)

  def __repr__(self):
    return '\n'.join([f'{edge[0]} -> {edge[1]}' for edge in self.edges])
