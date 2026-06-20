# graph_generator.py
# Contém:
# geração de grafos esparsos
# geração de grafos densos
# pesos aleatórios

import random
import math

def gerar_grafo_esparso(num_vertices):
    arestas = []
    arestas_usadas = set()


    for i in range(num_vertices - 1):
        peso = random.randint(1, 100)
        arestas.append((i, i + 1, peso))
        arestas_usadas.add((i, i + 1))

    arestas_extras = num_vertices

    while arestas_extras > 0:
        u = random.randint(0, num_vertices - 1)
        v = random.randint(0, num_vertices - 1)

        if u == v:
            continue

        aresta = tuple(sorted((u, v)))

        if aresta in arestas_usadas:
            continue

        arestas_usadas.add(aresta)
        peso = random.randint(1, 100)
        arestas.append((u, v, peso))
        arestas_extras -= 1

    return arestas


def gerar_grafo_denso(num_vertices):
    arestas = []

    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            peso = random.randint(1, 100)
            arestas.append((i, j, peso))

    return arestas

def gerar_grafo_geometrico(num_vertices):
    pontos = []

    for _ in range(num_vertices):
        x = random.uniform(0, 1000)
        y = random.uniform(0, 1000)
        pontos.append((x, y))

    arestas = []

    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            x1, y1 = pontos[i]
            x2, y2 = pontos[j]
            distancia = math.sqrt(
                (x1 - x2) ** 2 +
                (y1 - y2) ** 2
            )

            arestas.append((i, j, distancia))

    return arestas