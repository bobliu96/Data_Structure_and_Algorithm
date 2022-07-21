from pandas import array


def insertion_sort(arr):
    for i in range(1, len(arr)):
        pivot = arr[i]
        j = i-1
        while j >= 0 and pivot < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = pivot
    return arr

array = [6, 5, 2, 3, 1, 7, 9]
print(insertion_sort(array))