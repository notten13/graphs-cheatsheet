# Graphs Cheatsheet

A personal cheatsheet about graphs with common algorithms implemented in Python.

Not using any libraries (including numpy or specialised graph libraries) on purpose!

## Representing graphs

There are several common ways to represent a graph:

1. **Edge list**: very simple, we list all the edges in the graph - for example [(A, B), (B, C)]. It's very space-efficient for sparse graphs (few edges compared to the number of nodes), but avoid for dense graphs. It will also not be the most efficient if common operations are edge and neighbour lookups.

2. **Adjacency list**: A list of nodes, and for each node we list its neighbours.

3. **Adjacency matrix**: For n nodes, a 2D n*n matrix where if nodes i and j are connected, the value at position (i,j) should be 1. It's very efficient for edge and neighbour lookups, but always be mindful for sparse graphs (few edges compared to the number of nodes), as it will be very space inefficient (lots of 0s...)

4. **Incidence matrix**: TODO

## Traversing graphs

1. TODO: DFS
2. TODO: BFS

## Topological sorting

TODO
