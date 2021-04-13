# Search methods

import search

ab = search.GPSProblem('A', 'B'
                       , search.romania)
print("Busqueda en anchura")
A = search.breadth_first_graph_search(ab)
print("Recorrido:", A.path())
print("Coste:", A.path_cost)
print("\n")

print("Busqueda en profundidad")
B = search.depth_first_graph_search(ab)
print("Recorrido:", B.path())
print("Coste:", B.path_cost)
print("\n")

print("Busqueda ramificacion y acotacion")
C = search.ram_graph_search(ab)
print("Recorrido:", C.path())
print("Coste:", C.path_cost)
print("\n")

print("Busqueda ramificacion y acotacion con heuristica")
D = search.ram_with_h_graph_search(ab)
print("Recorrido:", D.path())
print("Coste:", D.path_cost)

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
