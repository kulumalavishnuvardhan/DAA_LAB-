# Selection Sort without using built-in sorting functions
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

# Selection Sort
for i in range(n - 1):
    min_index = i

    for j in range(i + 1, n):
        if arr[j] < arr[min_index]:
            min_index = j

    # Swap elements
    temp = arr[i]
    arr[i] = arr[min_index]
    arr[min_index] = temp

# End Time
end_time = time.perf_counter()

execution_time = end_time - start_time

# Output
print("Sorted List:", arr)
print("Execution Time:", execution_time, "seconds")

# Time Complexity
print("\nTime Complexity:")
print("Best Case    : O(n²)")
print("Average Case : O(n²)")
print("Worst Case   : O(n²)")
print("Space Complexity: O(1)")