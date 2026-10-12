# Bubble Sort without using built-in sorting functions
# Takes input from user, shows execution time and time complexity

import time

# Input from user
n = int(input("Enter the number of elements: "))

arr = []
for i in range(n):
    num = int(input(f"Enter element {i + 1}: "))
    arr.append(num)

print("Original List:", arr)

# Start execution time
start_time = time.perf_counter()

# Bubble Sort Algorithm
for i in range(n - 1):
    for j in range(n - 1 - i):
        if arr[j] > arr[j + 1]:
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp

# End execution time
end_time = time.perf_counter()

# Calculate execution time
execution_time = end_time - start_time

print("Sorted List:", arr)
print("Execution Time:", execution_time, "seconds")

# Time Complexity
print("\nTime Complexity:")
print("Best Case    : O(n)")
print("Average Case : O(n^2)")
print("Worst Case   : O(n^2)")
print("Space Complexity: O(1)")