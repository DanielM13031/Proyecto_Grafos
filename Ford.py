import networkx as nx

def grafo_residual(G):
    Gr =  nx. DiGraph()

    for u, v, data in G.edges(data = True):
        capacidad = data["capacity"]
        Gr.add_edge(u, v, capacity = capacidad)
        Gr.add_edge(v, u, capacity = 0)
    return Gr


def Ford_Fulkerson(G,s,t):

    Gf = grafo_residual(G)
    flujo_t  =  0

    while True:
        camino = DFS(Gf,s,t)

        if not camino:
            break

        capacidad_residual = min(Gf[u][v]['capacity'] for u, v in camino)
        flujo_t += capacidad_residual

        for u, v in camino:
            Gf[u][v]['capacity'] -= capacidad_residual
            Gf[v][u]['capacity'] += capacidad_residual
    return flujo_t