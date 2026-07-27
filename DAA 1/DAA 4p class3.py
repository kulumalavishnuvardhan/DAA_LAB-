# Insertion Sort without using built-in sorting functions
# User Input, Execution Time, and Time Complexity

import time

# User Input
n = int(input("Enter the number of elements: "))

arr = []
for i in range(n):
    num = int(input(f"Enter element {i + 1}: "))
    arr.append(num)

print("Original List:", arr)

# Start Time
start_time = time.perf_counter()

# Insertion Sort
for i in range(1, n):
    key = arr[i]
    j = i - 1

    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = key

# End Time
end_time = time.perf_counter()

execution_time = end_time - start_time

# Output
print("Sorted List:", arr)
print("Execution Time:", execution_time, "seconds")

# Time Complexity
print("\nTime Complexity:")
print("Best Case    : O(n)")
print("Average Case : O(n²)")
print("Worst Case   : O(n²)")
print("Space Complexity: O(1)")