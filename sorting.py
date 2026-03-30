
import time
import sys

#safety measure - python's recursion limit is 1000 and quick sort can surpass that on reversed/sorted lists
#therefore, the limit must be raised
sys.setrecursionlimit(50000)

# SORTING ALGORITHMS

#bubble sort

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

#selection sort

def selectionSort(arr, size):
    for i in range(size - 1):
        min_index = i
        for j in range(i + 1, size):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

#insertion sort

def insertionSort(arr):
    n = len(arr)
    if n <= 1:
        return
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

#merge sort

def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = [0] * n1
    R = [0] * n2
    for i in range(n1):
        L[i] = arr[l + i]
    for j in range(n2):
        R[j] = arr[m + 1 + j]
    i = j = 0
    k = l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def mergeSort(arr, l, r):
    if l < r:
        m = l + (r - l) // 2
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)

#quick sort

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quickSort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quickSort(arr, low, p - 1)
        quickSort(arr, p + 1, high)

#heap sort

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

#wrapper functions (for algorithms that need one)

def selection_sort(arr):
    selectionSort(arr, len(arr))

def merge_sort(arr):
    if len(arr) > 1:
        mergeSort(arr, 0, len(arr) - 1)

def quick_sort(arr):
    if len(arr) > 1:
        quickSort(arr, 0, len(arr) - 1)

#algorithm dictionary
#maps a name to the function (wrapper if needed) of each algorithm

ALGORITHMS = {"Bubble Sort":bubbleSort,
              "Insertion Sort": insertionSort,
              "Heap Sort": heapSort,
              "Selection Sort":selection_sort,
              "Merge Sort":merge_sort,
              "Quick Sort":quick_sort}

#O(n^2) algorithms become imperceptible for giant lists
FASTER_ALGORITHMS = {"Heap Sort":heapSort,
                    "Merge Sort":merge_sort,
                    "Quick Sort":quick_sort}

#quick sort reaches the recursion limit and slows down the experiment in some cases
NO_QUICKSORT = {"Bubble Sort":bubbleSort,
              "Insertion Sort": insertionSort,
              "Heap Sort": heapSort,
              "Selection Sort":selection_sort,
              "Merge Sort":merge_sort}

FASTER_ALG_NO_QUICKSORT = {"Heap Sort":heapSort,
                            "Merge Sort":merge_sort}

ONLY_QUICKSORT = {"Quick Sort":quick_sort}

#BENCHMARK

def benchmark(algorithm_fn, data, n_runs=1):
    """
    works on copies of data so that it keeps the original data unchanged
    returns average time in seconds
    """
    total_time = 0.0
    for _ in range(n_runs):
        arr_copy = data.copy()
        start = time.perf_counter()
        algorithm_fn(arr_copy)
        end = time.perf_counter()
        total_time += (end - start)
    return total_time / n_runs
