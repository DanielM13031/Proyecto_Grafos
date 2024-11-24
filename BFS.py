def BFS(graph, start, end):
    V_t = {}  
    L = [start]  
    visitados = set() 

    while L:
        M = L.pop(0)
        visitados.add(M) 
        
        if M == end:  
            T = []
            while M:
                T.append(M)
                M = V_t.get(M, None)
            return list(reversed(T)) 

        for j in graph.neighbors(M):
            if j not in visitados and graph[M][j]['capacity'] > 0:  
                V_t[j] = M
                L.append(j)

    return None
