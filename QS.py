import random


def quicksort(arr):
    return qsort(arr, 0, len(arr))


def qsort(arr, min, max):
    if (max - min) < 2:
        return

    rand = random.randrange(min, max - 1)
    newPivotIndex = partition(arr, rand, min, max)

    qsort(arr, min, newPivotIndex)
    qsort(arr, newPivotIndex + 1, max)


def partition(arr, pivotIndex, min, max):
    arr[pivotIndex], arr[min] = arr[min], arr[pivotIndex]
    pivot = arr[min]
    i = min + 1

    for j in range(min + 1, max):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i = i + 1

    arr[min], arr[i - 1] = arr[i - 1], arr[min]
    return i - 1
