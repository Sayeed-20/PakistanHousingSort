# The implementation for mergesort was referenced from

# Merge two subarrays from arr
def merge(arr, left, mid, right):
    # Create X = arr[left..mid] & Y = arr[mid+1..right]
    n1 = mid - left + 1
    n2 = right - mid
    X = [n1]
    Y = [n2]

    for i in range(n1):
        X[i] = arr[left + i]
    for j in range(n2):
        Y[j] = arr[mid + 1 + j]

    # Merge the arrays X and Y into arr
    i = 0
    j = 0
    k = left

    while i < n1 and j < n2:
        if X[i] <= Y[j]:
            arr[k] = X[i]
            i += 1
        else:
            arr[k] = Y[j]
            j += 1
        k += 1

    # When we run out of elements in either X or Y append the remaining elements
    while i < n1:
        arr[k] = X[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = Y[j]
        j += 1
        k += 1


def mergeSort(arr, left, right):
    if left < right:
        # m is the point where the array is divided into two subarrays
        mid = left + (right - left) / 2
        mergeSort(arr, left, mid)
        mergeSort(arr, mid + 1, right)

        # Merge the sorted subarrays
        merge(arr, left, mid, right)