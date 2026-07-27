# Merge Sort without using built-in sorting functions
# User Input, Execution Time, and Time Complexity

import time

# Merge Sort Function
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2

        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        # Merge the two halves
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # Copy remaining elements
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


# User Input
n = int(input("Enter the number of elements: "))

arr = []
for i in range(n):
    num = int(input(f"Enter element {i + 1}: "))
    arr.append(num)

print("Original List:", arr)

# Start Time
start_time = time.perf_counter()

# Sorting
merge_sort(arr)

# End Time
end_time = time.perf_counter()

execution_time = end_time - start_time

# Output
print("Sorted List:", arr)
print("Execution Time:", execution_time, "seconds")

# Time Complexity
print("\nTime Complexity:")
print("Best Case    : O(n log n)")
print("Average Case : O(n log n)")
print("Worst Case   : O(n log n)")
print("Space Complexity: O(n)")