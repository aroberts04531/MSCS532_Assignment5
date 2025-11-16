import random
import time
import sys

#Raising recursion limit 
sys.setrecursionlimit(5000)

# 1. Deterministic Quicksort (last element as pivot)

def partition(arr, low, high):
    """
    Deterministic partition uses the last element as the pivot.
    Rearranges arr[low:high+1] in order for
        -all elements <= pivot are on the left
        -all elements > pivot are on the right
    Is meant to return the final index of the pivot.
    """

    pivot = arr[high]
    i = low - 1 #index of the last element <= pivot

    for j in range(low, high):
        #if current element <= pivot, move it to the left section
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    #Places the pivot right after the last smaller element
    arr[i+1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort(arr, low, high):
    """
    Deterministic Quicksort recursively partitions and sorts the array in-place.
    """

    if low < high:
        #This partitions the array and get the pivot index  
        pivot_index = partition(arr, low, high)
        quicksort(arr, low, pivot_index -1)
        quicksort(arr, pivot_index + 1, high)

def test_deterministic_sort():
    """
    Simple test for deterministic Quicksort.
    """
    data = [10, 7, 8, 9, 1, 5]
    print("Deterministic test:")
    print("Original:", data)
    quicksort(data, 0, len(data) - 1)
    print(" Sorted:  ", data)

# 2. Randomized Quicksort (random pivot)

def random_partition(arr, low, high):
    """
    Randomized partition: 
    This chooses a random pivot index between low and high, 
    swaps it with the last element, then calls partition.
    """
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    return partition(arr, low, high)

def randomized_quicksort(arr, low, high):
    """
    Randomized Quicksort: 
    It uses a random pivot to reduce the chance of worst-case behavior.
    """
    if low < high:
        pivot_index = random_partition(arr, low, high)
        randomized_quicksort(arr, low, pivot_index - 1)
        randomized_quicksort(arr, pivot_index + 1, high)

def test_randomized_sort():
    """
    Simple test for randomized Quicksort.
    """
    data = [10, 7, 8, 9, 1, 5]
    print("Randomized test:")
    print(" Original: ", data)
    randomized_quicksort(data, 0, len(data) -1)
    print(" Sorted ", data)

# 3. Empirical Comparison

def generate_array(n, case_type="random"):
    """
    Generates an array of size n of different types:
    'random': random integers
    'sorted': sorted in non-decreasing order
    'reverse': sorted in decreasing order
    """
    if case_type == "random":
        arr = [random.randint(0, 100000) for _ in range(n)]
    else:
        base = [random.randint(0, 100000) for _ in range(n)]
        base.sort()
        if case_type == "sorted":
            arr = base
        elif case_type == "reverse":
            arr = list(reversed(base))
        else:
            raise ValueError("Unknown case_type: " + case_type)
    return arr

def time_sorting_function(sort_func, arr):
    """
    Times a sorting function that takes (arr, low, high)
    and returns the elapsed time in seconds.
    """
    start = time.perf_counter()
    sort_func(arr, 0, len(arr) - 1)
    end = time.perf_counter()
    return end - start

def empirical_comparison():
    """
    This empirically compares deterministic vs randomized Quicksort
    on different input sizes and distributions.
    """
     #reduced sizes to avoid huge recursion depth
    sizes = [100, 500] 
    case_types = ["random", "sorted", "reverse"]

    print("\nEmpirical Comparison: Deterministic vs Randomized Quicksort")
    print("-------------------------------------------------------------")
    print("Size\tCase\t\tDeterministic (s)\tRandomized (s)")

    for n in sizes:
        for case in case_types:
            base_arr = generate_array(n, case)

            arr_det = base_arr.copy()
            arr_rand = base_arr.copy()

            t_det = time_sorting_function(quicksort, arr_det)
            t_rand = time_sorting_function(randomized_quicksort, arr_rand)

            case_label = case if case != "reverse" else "reverse-sorted"
            print(f"{n}\t{case_label:12}\t{t_det:.6f}\t\t{t_rand:.6f}")

# 4. Main Entry Point

if __name__ == "__main__":
    #tests to show correctness
    test_deterministic_sort()
    print()
    test_randomized_sort()

    empirical_comparison()


