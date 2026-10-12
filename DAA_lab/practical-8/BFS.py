# Implementation of Graph and Breadth First Search (BFS)

# Number of vertices
vertices = 6

# Graph represented using an adjacency matrix
graph = [
    [0, 1, 1, 0, 0, 0],
    [1, 0, 0, 1, 1, 0],
    [1, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 1],
    [0, 0, 1, 1, 1, 0]
]

# BFS function
def bfs(graph, start):
    visited = [False] * vertices
    queue = [0] * vertices

    front = 0
    rear = 0

    # Mark starting vertex as visited
    visited[start] = True
    queue[rear] = start
    rear = rear + 1

    print("BFS Traversal:", end=" ")

    while front < rear:
        current = queue[front]
        front = front + 1

        print(current, end=" ")

        # Check all adjacent vertices
        i = 0
        while i < vertices:
            if graph[current][i] == 1 and visited[i] == False:
                visited[i] = True
                queue[rear] = i
                rear = rear + 1

            i = i + 1


# Display the graph
print("Graph:")
i = 0

while i < vertices:
    j = 0

    while j < vertices:
        print(graph[i][j], end=" ")
        j = j + 1

    print()
    i = i + 1

# Start BFS from vertex 0
bfs(graph, 0)