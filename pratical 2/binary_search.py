def binary_search(arr, target):
    """Search a sorted list for target using binary search."""
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def main():
    print("Binary Search Demo")
    input_values = input("Enter sorted integers separated by spaces: ").strip().split()
    arr = []
    for value in input_values:
        try:
            arr.append(int(value))
        except ValueError:
            print(f"Skipping invalid number: {value}")

    if not arr:
        print("No valid numbers were entered.")
        return

    try:
        target = int(input("Enter the integer to search for: ").strip())
    except ValueError:
        print("Please enter a valid integer to search.")
        return

    index = binary_search(arr, target)
    if index != -1:
        print(f"Target {target} found at index {index}.")
    else:
        print(f"Target {target} not found in the list.")


if __name__ == "__main__":
    main()
