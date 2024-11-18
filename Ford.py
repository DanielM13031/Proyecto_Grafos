import networkx as nx
from BFS import BFS

def grafo_residual(G):
    Gr =  nx. DiGraph()

    for u, v, data in G.edges(data = True):
        capacidad = data["capacity"]
        Gr.add_edge(u, v, capacity = capacidad)
        Gr.add_edge(v, u, capacity = 0)
    return Gr


def Ford_Fulkerson(G, s, t):
    Gf = grafo_residual(G)  
    flujo_t = 0

    while True:
        camino = BFS(Gf, s, t)  

        if not camino:  
            break

        capacidad_residual = float('Inf')
        for i in range(len(camino) - 1):  
            u, v = camino[i], camino[i + 1]
            capacidad_residual = min(capacidad_residual, Gf[u][v]['capacity'])

        flujo_t += capacidad_residual 


        for i in range(len(camino) - 1):
            u, v = camino[i], camino[i + 1]
            Gf[u][v]['capacity'] -= capacidad_residual  
            Gf[v][u]['capacity'] += capacidad_residual 

    return flujo_t