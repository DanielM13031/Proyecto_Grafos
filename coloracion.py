import networkx as nx

def coloreo_voraz(g):
    colores = {}
    for nodo in g.nodes():
        colores_usados = {colores[vecino] for vecino in g.neighbors(nodo) if vecino in colores}
        color = 0
        while color in colores_usados:
            color += 1
        colores[nodo] = color
    return colores
