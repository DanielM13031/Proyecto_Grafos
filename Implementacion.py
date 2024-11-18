import networkx as nx

#Definicion del grafo
G =  nx.DiGraph()

G.add_edge('A','B', capacity = 500)
G.add_edge('A','C', capacity = 400)
G.add_edge('B','D', capacity = 600)
G.add_edge('C','D', capacity = 350)
G.add_edge('D','E', capacity = 300)
G.add_edge('B','E', capacity = 250)
G.add_edge('E','F', capacity = 450)
G.add_edge('F','G', capacity = 500)
G.add_edge('G','H', capacity = 400)
G.add_edge('H','I', capacity = 550)
G.add_edge('I','J', capacity = 600)
G.add_edge('J','K', capacity = 500)
G.add_edge('K','L', capacity = 450)
G.add_edge('F','I', capacity = 350)
G.add_edge('A','G', capacity = 300)
G.add_edge('C','H', capacity = 250)
G.add_edge('E','J', capacity = 400)
G.add_edge('D','K', capacity = 500)
G.add_edge('B','L', capacity = 450)

#Flujos maximos
flow_value, flow_dict = nx.maximum_flow(G, 'A', 'D')
print("Flujo máximo:", flow_value)
print("Flujos por nodo:", flow_dict)


