import networkx as nx

def coloreo_voraz(g):
    colores = {}  # Diccionario para almacenar el color asignado a cada nodo
    for nodo in g.nodes():
        # Encuentra los colores ya asignados a los vecinos salientes
        colores_usados = {colores[vecino] for vecino in g.neighbors(nodo) if vecino in colores}
        # Encuentra el primer color no usado
        color = 0
        while color in colores_usados:
            color += 1
        # Asigna el color al nodo actual
        colores[nodo] = color
    return colores
