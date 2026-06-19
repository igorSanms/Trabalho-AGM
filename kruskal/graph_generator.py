# graph_generator.py
# Contém:
# geração de grafos esparsos
# geração de grafos densos
# pesos aleatórios

import random
import math

def generate_sparse_graph(num_vertices):
    edges = []
    used_edges = set()


    for i in range(num_vertices - 1):
        weight = random.randint(1, 100)
        edges.append((i, i + 1, weight))
        used_edges.add((i, i + 1))

    extra_edges = num_vertices

    while extra_edges > 0:
        u = random.randint(0, num_vertices - 1)
        v = random.randint(0, num_vertices - 1)

        if u == v:
            continue

        edge = tuple(sorted((u, v)))

        if edge in used_edges:
            continue

        used_edges.add(edge)
        weight = random.randint(1, 100)
        edges.append((u, v, weight))
        extra_edges -= 1

    return edges


def generate_dense_graph(num_vertices):
    edges = []

    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            weight = random.randint(1, 100)
            edges.append((i, j, weight))

    return edges

def generate_geometric_graph(num_vertices):
    points = []

    for _ in range(num_vertices):
        x = random.uniform(0, 1000)
        y = random.uniform(0, 1000)
        points.append((x, y))

    edges = []

    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            x1, y1 = points[i]
            x2, y2 = points[j]
            distance = math.sqrt(
                (x1 - x2) ** 2 +
                (y1 - y2) ** 2
            )

            edges.append((i, j, distance))

    return edges