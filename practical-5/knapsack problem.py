# 0/1 Knapsack Problem using Dynamic Programming

weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5

n = 4

# Create DP table
dp = []

for i in range(n + 1):
    row = []
    for j in range(capacity + 1):
        row.append(0)
    dp.append(row)

# Fill DP table
for i in range(1, n + 1):
    for w in range(1, capacity + 1):
        if weights[i - 1] <= w:
            include = values[i - 1] + dp[i - 1][w - weights[i - 1]]
            exclude = dp[i - 1][w]

            if include > exclude:
                dp[i][w] = include
            else:
                dp[i][w] = exclude
        else:
            dp[i][w] = dp[i - 1][w]

# Print DP table
print("DP Table:")
for i in range(n + 1):
    for j in range(capacity + 1):
        print(dp[i][j], end=" ")
    print()

# Maximum value
print("\nMaximum Profit:", dp[n][capacity])