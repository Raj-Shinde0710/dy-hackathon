def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1


def binary_search(arr, key):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1


ids = [101, 103, 105, 107, 109]
print("IDs:", ids)

key = 107
print("\nLinear Search Result:", linear_search(ids, key))
print("Binary Search Result:", binary_search(ids, key))
