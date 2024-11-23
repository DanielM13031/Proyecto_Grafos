import networkx as nx
from Ford import Ford_Fulkerson
from coloracion import coloreo_voraz
import matplotlib.pyplot as plt
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

G_ND = nx.Graph()
G_ND.add_edge('A','B')
G_ND.add_edge('B','C')
G_ND.add_edge('C','D')
G_ND.add_edge('D','E')
G_ND.add_edge('E','J')
G_ND.add_edge('A','F')
G_ND.add_edge('F','G')
G_ND.add_edge('G','H')
G_ND.add_edge('H','I')
G_ND.add_edge('I','J')
G_ND.add_edge('J','K')
G_ND.add_edge('K','L')
G_ND.add_edge('B','H')
G_ND.add_edge('F','H')
G_ND.add_edge('C','G')
G_ND.add_edge('E','K')
G_ND.add_edge('D','L')

#Flujos maximos
flow_value = Ford_Fulkerson(G, 'A', 'D')
print("Flujo maximo:", flow_value)
#Coloracion
coloracion = coloreo_voraz(G_ND)
node_colors = [coloracion[nodo] for nodo in G_ND.nodes()]
print(coloracion)

# Visualización del grafo
pos = nx.spring_layout(G)  
nx.draw(G, pos, with_labels=True, node_size=700, node_color=node_colors, font_size=10, font_weight="bold")
edge_labels = nx.get_edge_attributes(G, 'capacity')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.title("Grafo dirigido con capacidades")
plt.show()
