import time

# Heapify function
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Check left child
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check right child
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Swap and continue heapifying if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

# Heap Sort function
def heap_sort(arr):
    n = len(arr)

    # Build Max Heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

# User input
n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    arr.append(element)

# Measure execution time
start_time = time.time()

heap_sort(arr)

end_time = time.time()

# Output
print("\nSorted Array:")
for num in arr:
    print(num, end=" ")

print("\n\nTime Complexity:")
print("Best Case   : O(n log n)")
print("Average Case: O(n log n)")
print("Worst Case  : O(n log n)")

print(f"\nExecution Time: {end_time - start_time:.6f} seconds")
