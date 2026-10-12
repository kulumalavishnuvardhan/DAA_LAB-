# Kruskal's Algorithm (Without User Input)

class Edge:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w


# Find parent of a node
def find(parent, i):
    while parent[i] != i:
        i = parent[i]
    return i


# Union of two sets
def union(parent, x, y):
    x_root = find(parent, x)
    y_root = find(parent, y)
    parent[x_root] = y_root


# Kruskal's Algorithm
def kruskal(vertices, edges):
    # Manual sorting of edges (Bubble Sort)
    n = len(edges)
    for i in range(n):
        for j in range(0, n - i - 1):
            if edges[j].w > edges[j + 1].w:
                temp = edges[j]
                edges[j] = edges[j + 1]
                edges[j + 1] = temp

    parent = []
    for i in range(vertices):
        parent.append(i)

    print("Edges in Minimum Spanning Tree:")
    total_cost = 0
    count = 0

    i = 0
    while count < vertices - 1:
        edge = edges[i]
        i += 1

        x = find(parent, edge.u)
        y = find(parent, edge.v)

        if x != y:
            print(edge.u, "--", edge.v, "=", edge.w)
            total_cost += edge.w
            union(parent, x, y)
            count += 1

    print("Total Cost of MST:", total_cost)


# Graph Definition
vertices = 4

edges = [
    Edge(0, 1, 10),
    Edge(0, 2, 6),
    Edge(0, 3, 5),
    Edge(1, 3, 15),
    Edge(2, 3, 4)
]

kruskal(vertices, edges)