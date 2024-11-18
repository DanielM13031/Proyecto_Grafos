import networkx as nx

def BFS(graph, start, end):
    V_t = {}
    L = [start]  

    while L:
        M = L.pop(0)

        if M == end:
            T = []
            while M:
                T.append(M)
                M = V_t.get(M, None)
            return list(reversed(T))

        for j in graph.neighbors(M):
                V_t[j] = M  
                L.append(j)




