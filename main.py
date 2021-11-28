import os
import time
import numpy as np

from QS import quicksort as QuickSort
from HeapSort import heapSort as HeapSort
from MergeSort import mergeSort as MergeSort
from CountSort import count_sort as CountSort

os.system("MakeFiles.py")

size = np.load("random_arr.npy").size


def QS_TimeTest(name):
    arr = np.load(name)
    begin = time.time()
    QuickSort(arr)
    end = time.time()
    if sorted(arr):
        return end - begin
    return "ERROR"


def HeapSort_TimeTest(name):
    arr = np.load(name)
    begin = time.time()
    HeapSort(arr)
    end = time.time()
    if sorted(arr):
        return end - begin
    return "ERROR"


def MergeSort_TimeTest(name):
    arr = np.load(name)
    begin = time.time()
    MergeSort(arr)
    end = time.time()
    if sorted(arr):
        return end - begin
    return "ERROR"


def Sort2_TimeTest(name):
    arr = np.load(name)
    begin = time.time()
    CountSort(arr)
    end = time.time()
    if sorted(arr):
        return end - begin
    return "ERROR"


print("\nQS (ver.Lomuto)")
print(f'Random: \t {QS_TimeTest("random_arr.npy")} sec')
print(f'Sorted: \t {QS_TimeTest("sorted_arr.npy")} sec')
print(f'Reversed: \t {QS_TimeTest("reverse_sorted_arr.npy")} sec')

print("\nHeapSort")
print(f'Random: \t {HeapSort_TimeTest("random_arr.npy")} sec')
print(f'Sorted: \t {HeapSort_TimeTest("sorted_arr.npy")} sec')
print(f'Reversed: \t {HeapSort_TimeTest("reverse_sorted_arr.npy")} sec')

print("\nMergeSort")
print(f'Random: \t {MergeSort_TimeTest("random_arr.npy")} sec')
print(f'Sorted: \t {MergeSort_TimeTest("sorted_arr.npy")} sec')
print(f'Reversed: \t {MergeSort_TimeTest("reverse_sorted_arr.npy")} sec')

print("\nCountSort")
print(f'Random: \t {Sort2_TimeTest("random_arr.npy")} sec')
print(f'Sorted: \t {Sort2_TimeTest("sorted_arr.npy")} sec')
print(f'Reversed: \t {Sort2_TimeTest("reverse_sorted_arr.npy")} sec')
