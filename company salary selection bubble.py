def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


# Main program
salaries = [45000, 25000, 60000, 40000, 30000]

print("Original:", salaries)
print("\nBubble Sort:", bubble_sort(salaries.copy()))
print("Selection Sort:", selection_sort(salaries.copy()))
print("\nTop 5 Salaries:", sorted(salaries)[-5:])
