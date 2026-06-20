# prim.py
# Contém:
# Algoritmo de Prim
# Fila de Prioridade (heapq)

import heapq

def prim(num_vertices, arestas):

    adj = [[] for _ in range(num_vertices)]

    for u, v, peso in arestas:
        adj[u].append((peso, v))
        adj[v].append((peso, u))

    mst = []
    peso_total = 0
    visitados = [False] * num_vertices

    min_heap = [(0, 0, -1)]

    while min_heap:
        peso, u, pai = heapq.heappop(min_heap)

        if visitados[u]:
            continue

        visitados[u] = True
        peso_total += peso

        if pai != -1:
            mst.append((pai, u, peso))

        if len(mst) == num_vertices - 1:
            break

        for proximo_peso, v in adj[u]:
            if not visitados[v]:
                heapq.heappush(min_heap, (proximo_peso, v, u))

    return mst, peso_total