# kruskal.py
# Contém:
# Union Find
# Algoritmo de Kruskal

class UnionFind:

    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):

        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, a, b):

        root_a = self.find(a)
        root_b = self.find(b)

        if root_a == root_b:
            return False

        if self.rank[root_a] < self.rank[root_b]:
            self.parent[root_a] = root_b

        elif self.rank[root_a] > self.rank[root_b]:
            self.parent[root_b] = root_a

        else:
            self.parent[root_b] = root_a
            self.rank[root_a] += 1

        return True


def kruskal(num_vertices, edges):

    edges = sorted(edges, key=lambda edge: edge[2])

    uf = UnionFind(num_vertices)

    mst = []
    total_weight = 0

    for u, v, weight in edges:

        if uf.union(u, v):

            mst.append((u, v, weight))
            total_weight += weight

            if len(mst) == num_vertices - 1:
                break

    return mst, total_weight