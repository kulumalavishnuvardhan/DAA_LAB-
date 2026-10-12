# Implementation of Graph and DFS

class Graph:
    def __init__(self):
        self.vertices = 6

        # Adjacency Matrix
        self.graph = [
            [0, 1, 1, 0, 0, 0],
            [1, 0, 0, 1, 1, 0],
            [1, 0, 0, 0, 1, 0],
            [0, 1, 0, 0, 0, 1],
            [0, 1, 1, 0, 0, 1],
            [0, 0, 0, 1, 1, 0]
        ]

    def dfs(self, start):
        visited = [0] * self.vertices

        print("DFS Traversal:")
        self.dfs_util(start, visited)

    def dfs_util(self, vertex, visited):
        visited[vertex] = 1
        print(vertex, end=" ")

        for i in range(self.vertices):
            if self.graph[vertex][i] == 1 and visited[i] == 0:
                self.dfs_util(i, visited)


g = Graph()
g.dfs(0)