import time

def matrix_chain_order(p):
    n = len(p) - 1

    # Create DP table
    m = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(0)
        m.append(row)

    # Chain length
    L = 2
    while L <= n:
        i = 0
        while i <= n - L:
            j = i + L - 1
            m[i][j] = 999999999

            k = i
            while k < j:
                cost = m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j + 1]

                if cost < m[i][j]:
                    m[i][j] = cost

                k += 1

            i += 1

        L += 1

    return m[0][n - 1]


# User Input
n = int(input("Enter number of matrices: "))

dimensions = []
print("Enter dimensions array (size =", n + 1, ")")

for i in range(n + 1):
    dimensions.append(int(input()))

# Start timer
start_time = time.perf_counter()

result = matrix_chain_order(dimensions)

# End timer
end_time = time.perf_counter()

execution_time = end_time - start_time

print("\nMinimum number of multiplications:", result)
print("Execution Time:", execution_time, "seconds")

print("\nTime Complexity: O(n^3)")
print("Space Complexity: O(n^2)")