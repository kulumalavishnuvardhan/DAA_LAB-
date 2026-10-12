# Prim's Algorithm (Without User Input)

# Graph represented using adjacency matrix
graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

vertices = 5

selected = [False, False, False, False, False]

selected[0] = True

edges = 0
total_cost = 0

print("Edge \tWeight")

while edges < vertices - 1:
    minimum = 9999
    x = 0
    y = 0

    i = 0
    while i < vertices:
        if selected[i]:
            j = 0
            while j < vertices:
                if (not selected[j]) and graph[i][j] != 0:
                    if graph[i][j] < minimum:
                        minimum = graph[i][j]
                        x = i
                        y = j
                j += 1
        i += 1

    print(str(x) + " - " + str(y) + "\t" + str(graph[x][y]))

    total_cost += graph[x][y]
    selected[y] = True
    edges += 1

print("Total Cost of MST =", total_cost)