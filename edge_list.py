class EdgeList:
  def __init__(self):
    self.edges = []

  def add_edge(self, edge):
    self.edges.append(edge)

  def __repr__(self):
    return '\n'.join([f'{edge[0]} -> {edge[1]}' for edge in self.edges])
