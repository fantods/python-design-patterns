# worst-case: O(n^2)
# find smallest element and swap it with the first element in the array
# continue until sorted
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = 1
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j

        arr[i], a[min_idx] = arr[min_idx], arr[i]
