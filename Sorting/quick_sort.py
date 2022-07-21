def partiton(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def quick_sort(arr, low, high):
    if low < high:
        pa = partiton(arr, low, high)
        quick_sort(arr, low, pa - 1)
        quick_sort(arr, pa + 1, high)
    else:
        return

array = [6, 5, 2, 3, 1, 7, 9]
quick_sort(array, 0, len(array)-1)
print(array)