import networkx as nx
from Ford import Ford_Fulkerson

#Definicion del grafo
G =  nx.DiGraph()

G.add_edge('A','B', capacity = 500)
G.add_edge('B','C', capacity = 400)
G.add_edge('C','D', capacity = 600)
G.add_edge('D','E', capacity = 350)
G.add_edge('E','J', capacity = 300)
G.add_edge('A','F', capacity = 450)
G.add_edge('F','G', capacity = 500)
G.add_edge('G','H', capacity = 400)
G.add_edge('H','I', capacity = 550)
G.add_edge('I','J', capacity = 600)
G.add_edge('J','K', capacity = 500)
G.add_edge('K','L', capacity = 450)
G.add_edge('B','H', capacity = 350)
G.add_edge('F','H', capacity = 300)
G.add_edge('C','G', capacity = 250)
G.add_edge('E','K', capacity = 400)
G.add_edge('D','L', capacity = 500)

#Flujos maximos
flow_value = Ford_Fulkerson(G, 'A', 'D')
print("Flujo maximo:", flow_value)





