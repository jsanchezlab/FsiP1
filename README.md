# FsiP1
Para la realización de esta práctica se han realizado las siguiente modificaciones:

1.1 Ramificación y acotación
Se ha creado en utils.py una nueva clase de cola "PriorityQueue" que se ordena al realizar cualquier inserción en base al coste del camino. 
En search.py se ha añadido el tipo de búsqueda "ram_graph_search" que hace uso de "PriorityQueue" y por tanto realiza una búsqueda por ramificación y acotación

1.2 Ramifiación y acotación con heurística
Se ha creado en utils.py una nueva clase de cola "HQueue" que se ordena al realizar cualquier inserción en base al coste del camino + la heurística que determina la distancia del nodo en el que nos encontramos al nodo objetivo. 
En search.py se ha añadido el tipo de búsqueda "ram_with_h_graph_search" que hace uso de "HQueue" y por tanto realiza una búsqueda por ramificación y acotación con heurística.
Para poder hacer uso del método h() de la clase problem, al usar "HQueue" debemos pasarle como parametro "problem", que hace referencia al problema que vamos a resolver

Observando los resultados de los diferentes algoritmos de búsqueda llegamos a las siguientes conclusiones:
-Ramificación y acotación consigue encontrar la solución óptima al problema puesto que siempre irá por el camino con menor coste.
-Sin embargo, para llegar a la solución recorre considerablemente más nodos que la búsqueda en profundidad y la búsqueda en anchura.
-Haciendo uso de la heurística conseguimos un algoritmo que también llega a la solución óptima y, además, expande menos nodos que el resto de algortimos.
