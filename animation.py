from manim import *

class Grafo(Scene):
    def construct(self):
        Texto1 = Text("Aplicación de grafos a Redes")
        self.play(Write(Texto1))
        self.wait(1)
        letras = Texto1.submobjects[:12]
        otras = Texto1.submobjects[12:]

        separacion = 1.5
        positions = {
            "A": [-4 * separacion, 3, 0],  # Nivel 1
            "B": [-2 * separacion, 3, 0],  # Nivel 1
            "C": [0 * separacion, 3, 0],   # Nivel 1
            "D": [-4 * separacion, 1, 0],  # Nivel 2
            "E": [-1 * separacion, 1, 0],  # Nivel 2
            "F": [2 * separacion, 1, 0],   # Nivel 2
            "G": [-4 * separacion, -1, 0], # Nivel 3
            "H": [-2 * separacion, -1, 0], # Nivel 3
            "I": [0 * separacion, -1, 0],  # Nivel 3
            "J": [2 * separacion, -1, 0],  # Nivel 3
            "K": [4 * separacion, -1, 0],  # Nivel 3
            "L": [-1 * separacion, -3, 0],  # Nivel 4
        }
        nodos = []
        for idx, (letra, pos) in enumerate(zip(letras, positions.values())):
            nodo = Circle(radius=0.25, color=WHITE).move_to(pos)
            nodos.append(nodo)

        self.play (*[FadeOut(letras) for letras in otras])
        self.play(*[Transform(letra, nodo) for letra, nodo in zip(letras, nodos)])
        edges = [
            ("A", "B"), ("B", "C"), ("C", "D"), ("D", "E"), ("E", "J"),
            ("A", "F"), ("F", "G"), ("G", "H"), ("H", "I"), ("I", "J"),
            ("J", "K"), ("K", "L"), ("B", "H"), ("F", "H"), ("C", "G"),
            ("E", "K"), ("D", "L"),
        ]

        edge_labels = {
            ("A", "B"): "900Mbps, 2.80ms",
            ("B", "C"): "1250Mbps, 4.12ms",
            ("C", "D"): "1450Mbps, 3.42ms",
            ("D", "E"): "1310Mbps, 4.74ms",
            ("E", "J"): "400Mbps, 2.33ms",
            ("A", "F"): "200Mbps, 1.00ms",
            ("F", "G"): "230Mbps, 1.00ms",
            ("G", "H"): "790Mbps, 2.98ms",
            ("H", "I"): "2090Mbps, 4.80ms",
            ("I", "J"): "1900Mbps, 4.17ms",
            ("J", "K"): "1430Mbps, 3.86ms",
            ("K", "L"): "880Mbps, 2.96ms",
            ("B", "H"): "900Mbps, 3.57ms",
            ("F", "H"): "650Mbps, 3.17ms",
            ("C", "G"): "510Mbps, 3.04ms",
            ("E", "K"): "580Mbps, 2.45ms",
            ("D", "L"): "570Mbps, 2.14ms",
        }

        label_positions = {
            ("C", "D"): [-1.5, 2.7, 0],
            ("D", "E"): [-4.2, 1.1, 0],
            ("E", "J"): [1.7, -0.2, 0],
            ("A", "F"): [1, 1.3, 0],
            ("F", "G"): [-1.8, 0.1, 0],
            ("G", "H"): [-4.5, -1.2, 0],
            ("H", "I"): [-1.6, -1.1, 0],
            ("I", "J"): [1.5, -0.9, 0],
            ("J", "K"): [4.5, -1.1, 0],
            ("K", "L"): [2, -2, 0],
            ("B", "H"): [-3.1, 0.27, 0],
            ("F", "H"): [-2, -0.4, 0],
            ("C", "G"): [-2.4, 1.6, 0],
            ("E", "K"): [3, 0, 0],
            ("D", "L"): [-2.5, -2, 0],
        }
        label_rotations = {
            ("A", "F"): -12,
            ("C", "D"): 20,
            ("C", "G"): 33,
            ("B", "H"): 90, 
            ("F", "G"): 13,
            ("F", "H"): 16,
            ("E", "J"): -21,
            ("D", "L"): -41,
            ("E", "K"): -18,
            ("K", "L"): 18,    

        }

        vertex_conf = {node:{"radius": 0.25} for node in positions.keys()}
        edges_conf = {edge: {"tip_length": 0.15}for edge in[("A", "B"), ("B", "C"), ("C", "D"), ("D", "E"), ("E", "J"),
                ("A", "F"), ("F", "G"), ("G", "H"), ("H", "I"), ("I", "J"),
                ("J", "K"), ("K", "L"), ("B", "H"), ("F", "H"), ("C", "G"),
                ("E", "K"), ("D", "L"),] }

        digraph = DiGraph(
            vertices = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"],
            edges = edges,
            layout = positions,
            labels = True,
            vertex_config = vertex_conf,
            edge_config = edges_conf
        )
        labels = {
            vertex: Text(vertex, font_size=0.01).move_to(positions[vertex]) for vertex in positions
        }

        self.play(*[Create(digraph[v]) for v in digraph.vertices])

        for label in labels.values():
            self.add(label)

        self.play(*[Create(digraph.edges[e]) for e in digraph.edges])

        label_texts = []
        for edge, label in edge_labels.items():
            if edge in label_positions:
                label_position = label_positions[edge]
            else:
                start, end = edge
                pos_start = positions[start]
                pos_end = positions[end]
                label_position = [(s + e) / 2 for s, e in zip(pos_start, pos_end)]
                label_position[1] += 0.1
                label_text = Text(label, font_size=10).move_to(label_position)
                label_texts.append(label_text)


            label_text = Text(label, font_size=10).move_to(label_position)

            if edge in label_rotations:
                label_text.rotate(label_rotations[edge] * DEGREES)

            self.play(FadeIn(label_text))
            self.add(label_text)


        self.wait(1)
        self.wait(2)



        camino1 = [("A", "B"), ("B", "C"), ("C", "D"), ("D", "L")]
        for edge in camino1:
            self.play(digraph.edges[edge].animate.set_color(RED))
            self.wait(0.5)

        for vertex in ["A", "B", "C", "D", "L"]:
            self.play(digraph[vertex].animate.set_color(YELLOW))
            self.wait(0.3)
        self.wait(1)


        camino2 = [("A", "F"), ("F", "H"), ("H", "I"), ("I", "J"), ("J", "K"), ("K", "L")]
        for edge in camino2:
            self.play(digraph.edges[edge].animate.set_color(BLUE))
            self.wait(0.5)

        for vertex in ["A", "F", "H", "I", "J", "K", "L"]:
            self.play(digraph[vertex].animate.set_color(RED))
            self.wait(0.3)
        self.wait(1)

        camino3 = [("A", "B"), ("B", "H"), ("H", "I"), ("I", "J"), ("J", "K"), ("K", "L")]
        for edge in camino3:
            self.play(digraph.edges[edge].animate.set_color(YELLOW))
            self.wait(0.5)

        for vertex in ["A", "B", "H", "I", "J", "K", "L"]:
            self.play(digraph[vertex].animate.set_color(GREEN))
            self.wait(0.3)
        self.wait(1)

        camino4 = [("A", "F"), ("F", "G"), ("G", "H"), ("H", "I"), ("I", "J"), ("J", "K"), ("K", "L")]
        for edge in camino4:
            self.play(digraph.edges[edge].animate.set_color(PURPLE))
            self.wait(0.5)

        for vertex in ["A", "F", "G", "H", "I", "J", "K", "L"]:
            self.play(digraph[vertex].animate.set_color(GRAY))
            self.wait(0.3)
        self.wait(2)

        self.clear()
        self.wait(1)

        code = Code(
            code ="""def Ford_Fulkerson(G, s, t):
                        Gf = grafo_residual(G)  
                        flujo_t = 0
                        caminos_usados = [] 
                        while True:
                            camino = BFS(Gf, s, t)  
                            if not camino:  
                                break
                            capacidad_residual = float('Inf')
                            for i in range(len(camino) - 1):
                                u, v = camino[i], camino[i + 1]
                                capacidad_residual = min(capacidad_residual, Gf[u][v]['capacity'])
                            caminos_usados.append((camino, capacidad_residual))
                            flujo_t += capacidad_residual
                            for i in range(len(camino) - 1):
                                u, v = camino[i], camino[i + 1]
                                Gf[u][v]['capacity'] -= capacidad_residual
                                Gf[v][u]['capacity'] += capacidad_residual
                        return flujo_t, caminos_usados""",
                        tab_width = 4,
                        language = "Python",
                        font_size = 10,
                        style = "dracula"
                    ) 
        self.play(Write(code))
        self.wait(2)