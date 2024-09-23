from algorithms.bubble_sort import bubble_sort
from algorithms.insertion_sort import insertion_sort
from algorithms.quick_sort import quick_sort
from utils.random_array import random_array
from utils.measure_time import measure_time

# Array sizes to test
sizes = [1000, 2000, 3000, 4000, 5000, 6000]

for size in sizes:
    arr = random_array(size)
    
    # Copy the array for each sort function to avoid sorting the same array multiple times
    arr_copy = arr.copy()
    bubble_time = measure_time(bubble_sort, arr_copy)
    
    arr_copy = arr.copy()
    insertion_time = measure_time(insertion_sort, arr_copy)
    
    arr_copy = arr.copy()
    quick_time = measure_time(lambda x: quick_sort(x), arr_copy)  # using lambda for quick_sort
    
    print(f'Array Size: {size}')
    print(f'Bubble Sort: {bubble_time:.2f} ms')
    print(f'Insertion Sort: {insertion_time:.2f} ms')
    print(f'Quick Sort: {quick_time:.2f} ms')
    print('-------------------------------')