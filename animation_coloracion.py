from manim import *

class Grafo_col(Scene):
    def construct(self):

        Texto = Text(
            "Coloración Voraz",
            t2c={
                "C": RED,
                "o": ORANGE,
                "l": YELLOW,
                "o2": GREEN,  # "o2" especifica la segunda aparición de "o"
                "r": BLUE,
                "a": PURPLE,
                "c": PINK,
                "i": GOLD,
                "ó": PURE_RED,
                "n": TEAL,
                "V": DARK_BLUE,
                "o3": PURE_GREEN,  # "o3" especifica la tercera aparición de "o"
                "r2": LIGHT_PINK,  # "r2" especifica la segunda aparición de "r"
                "a2": MAROON,      # "a2" especifica la segunda aparición de "a"
                "z": GRAY,
            },
        )
        Texto2 = Text("Grafo no dirigido asociado")


        letras = Texto.submobjects[:12]  


        self.play(Write(Texto))
        self.wait(1)


        self.play(Transform(Texto, Texto2))
        self.wait(1)


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


        self.play(*[Transform(letra, nodo) for letra, nodo in zip(letras, nodos)])
        self.play(FadeOut(Texto))



        edges = [
            ("A", "B"), ("B", "C"), ("C", "D"), ("D", "E"), ("E", "J"),
            ("A", "F"), ("F", "G"), ("G", "H"), ("H", "I"), ("I", "J"),
            ("J", "K"), ("K", "L"), ("B", "H"), ("F", "H"), ("C", "G"),
            ("E", "K"), ("D", "L"),
        ]


        graph = Graph(
            vertices=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"],
            edges=edges,
            layout=positions,
            labels=True,  
            vertex_config={"radius": 0.25},
        )


        self.play(*[Create(graph[v]) for v in graph.vertices])
        self.play(*[Create(graph.edges[e]) for e in graph.edges])
        self.wait(2)

        for vertex in ["A", "C", "E", "H", "L"]:
            self.play(graph[vertex].animate.set_color(PURE_BLUE))
        for vertex in ["B", "D", "J", "F"]:
            self.play(graph[vertex].animate.set_color(PURE_RED))
        for vertex in ["G", "I", "K"]:
            self.play(graph[vertex].animate.set_color(PURE_GREEN))
        self.wait(1)
        
        exclude_vertices = ["G", "H", "F"]
        exclude_edges = [("G", "H"), ("F", "G"), ("F", "H")]
        self.play(
            *[FadeOut(graph[v]) for v in graph.vertices if v not in exclude_vertices],
            *[FadeOut(graph.edges[e]) for e in graph.edges if e not in exclude_edges]
        )
        self.wait(2)

        self.play(
            *[FadeOut(graph[v]) for v in exclude_vertices],
            *[FadeOut(graph.edges[e]) for e in exclude_edges]
        )

        self.wait(1)
        formula1= MathTex(r"\omega(G) = 3 ")
        formula1.move_to(ORIGIN)
        self.play(Write(formula1))
        self.wait(1)

        formula2 = MathTex(r"3 \leq \chi(G)")
        formula2.move_to(ORIGIN)
        self.play(Transform(formula1, formula2))
        self.wait(1)
        formula3 = Tex(r"$\chi(G) \leq 4$, ", r"$G$ es simple $->$ ", r"$G$ es 4-coloreable")
        formula3.move_to(ORIGIN)
        self.play(FadeOut(formula1))
        self.play(FadeIn(formula3))
        self.wait(1)

        formula4 = MathTex(r"3 \leq \chi(G) \leq 4")
        self.play(Transform(formula3, formula4))
        self.wait(1)

        conclusion_text = MathTex(
            r"\text{Dadas estas cotas y por el algoritmo de coloración voraz, }",
            r"\text{se demuestra que } \chi(G) = 4."
        )
        conclusion_text.scale(0.7)
        self.play(FadeOut(formula3))
        self.play(FadeIn(conclusion_text))
        self.wait(2)
        self.play(FadeOut(conclusion_text))

        code = Code(
            code ="""def coloreo_voraz(g):
                        colores = {}
                        for nodo in g.nodes():
                            colores_usados = {colores[vecino] for vecino in g.neighbors(nodo) if vecino in colores}
                            color = 0
                            while color in colores_usados:
                                color += 1
                            colores[nodo] = color
                        return colores""",
                        tab_width = 4,
                        language = "Python",
                        font_size = 10,
                        style = "dracula"
                    ) 
        self.play(Write(code))
        self.wait(2)


