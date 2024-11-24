import networkx as nx
from Ford import Ford_Fulkerson
from coloracion import coloreo_voraz
from Latencia import Latencia_dinamica, Asignar_flujo, Calcular_rutas
import matplotlib.pyplot as plt


#Grafo de la red
G = nx.DiGraph()
G.add_edge('A', 'B', capacity=500, latency_base=1)
G.add_edge('B', 'C', capacity=400, latency_base=1)
G.add_edge('C', 'D', capacity=600, latency_base=1)
G.add_edge('D', 'E', capacity=350, latency_base=1)
G.add_edge('E', 'J', capacity=300, latency_base=1)
G.add_edge('A', 'F', capacity=450, latency_base=1)
G.add_edge('F', 'G', capacity=500, latency_base=1)
G.add_edge('G', 'H', capacity=400, latency_base=1)
G.add_edge('H', 'I', capacity=550, latency_base=1)
G.add_edge('I', 'J', capacity=600, latency_base=1)
G.add_edge('J', 'K', capacity=500, latency_base=1)
G.add_edge('K', 'L', capacity=450, latency_base=1)
G.add_edge('B', 'H', capacity=350, latency_base=1)
G.add_edge('F', 'H', capacity=300, latency_base=1)
G.add_edge('C', 'G', capacity=250, latency_base=1)
G.add_edge('E', 'K', capacity=400, latency_base=1)
G.add_edge('D', 'L', capacity=500, latency_base=1)

#Grafo no dirigido asociado al dirigido
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

server_traffic = {
    'A': 100, 'B': 150, 'C': 120, 'D': 200,
    'E': 80, 'F': 130, 'G': 110, 'H': 90,
    'I': 170, 'J': 140, 'K': 160, 'L': 180
}

# Factor de congestión
k = 1

# Calcular las rutas de menor latencia
Latencia_dinamica(G, k)
paths = Calcular_rutas(G, server_traffic)

# Asignar tráfico a las aristas según las rutas
Asignar_flujo(G, server_traffic, paths)

# Recalcular latencias dinámicas con el nuevo tráfico
Latencia_dinamica(G, k)

# Flujo máximo (opcional)
flow_value = Ford_Fulkerson(G, 'A', 'L')
print("Flujo máximo:", flow_value)

print()

# Coloración
coloracion = coloreo_voraz(G_ND)
node_colors = [coloracion[nodo] for nodo in G_ND.nodes()]
print("Coloración de nodos:", coloracion)

print()

# Mostrar latencias y Flujo
print("Flujo y latencias por enlace:")
for u, v, data in G.edges(data=True):
    print(f"Enlace {u}-{v}: Flujo = {data['traffic']} Mbps, Latencia Dinámica = {data['dynamic_latency']:.2f} ms")

# Visualización del grafo
pos = nx.spring_layout(G)
edge_labels = {
    (u, v): f"{data['traffic']} Mbps, {data['dynamic_latency']:.2f} ms"
    for u, v, data in G.edges(data=True)
}
nx.draw(G, pos, with_labels=True, node_size=700, node_color=node_colors, font_size=10, font_weight='bold')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.title("Grafo con tráfico y latencias dinámicas")
plt.show()


    