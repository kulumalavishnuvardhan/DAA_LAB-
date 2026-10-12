import time

# Dynamic Programming - Coin Change (Minimum Coins)

def coin_change(coins, amount):
    # Create DP array
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    # Fill DP table
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i and dp[i - coin] != float('inf'):
                if dp[i] > dp[i - coin] + 1:
                    dp[i] = dp[i - coin] + 1

    if dp[amount] == float('inf'):
        return -1
    return dp[amount]


# User Input
n = int(input("Enter number of coin denominations: "))

coins = []
print("Enter coin denominations:")
for i in range(n):
    coin = int(input())
    coins.append(coin)

amount = int(input("Enter the amount to make change for: "))

# Measure Execution Time
start_time = time.perf_counter()

result = coin_change(coins, amount)

end_time = time.perf_counter()

# Output
if result == -1:
    print("Change cannot be made with given coins.")
else:
    print("Minimum coins required:", result)

print(f"Execution Time: {(end_time - start_time):.8f} seconds")

# Time Complexity
print("Time Complexity: O(N × Amount)")
print("Space Complexity: O(Amount)")