import networkx as nx

def BFS (graf, start, end):
    T = []
    L = [start]
    while len(L) != 0:
        M = L.pop(0)
        T.append(M)

        if M == end:
            return T
        
        for j in graf.neighbors(M):
            if j not in L and j not in T:
                L.append(j)
    return T
