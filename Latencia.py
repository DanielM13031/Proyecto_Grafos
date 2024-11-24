import networkx as nx

def Latencia_dinamica(G, k):
    for u, v, data in G.edges(data=True):
        capacity = data['capacity']
        latency_base = data['latency_base']
        traffic = data.get('traffic', 0)
        if traffic <= capacity:
            dynamic_latency = latency_base
        else:
            dynamic_latency = latency_base + k * (traffic / capacity)
        data['dynamic_latency'] = dynamic_latency

def Asignar_flujo(G, server_traffic, paths):

    for u, v in G.edges():
        G[u][v]['traffic'] = 0

    for source, destinations in paths.items():
        for target, path in destinations.items():
            if path is not None:
                traffic = server_traffic[source]
                for i in range(len(path) - 1):
                    u, v = path[i], path[i + 1]
                    G[u][v]['traffic'] += traffic  

def Calcular_rutas(G, server_traffic):

    paths = {}
    for source in server_traffic.keys():
        paths[source] = {}
        for target in server_traffic.keys():
            if source != target:
                try:
                    path = nx.shortest_path(G, source=source, target=target, weight='dynamic_latency')
                    paths[source][target] = path
                except nx.NetworkXNoPath:
                    paths[source][target] = None
    return paths
