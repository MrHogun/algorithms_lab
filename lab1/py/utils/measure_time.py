import time

def measure_time(sort_func, arr):
    start_time = time.time()
    sort_func(arr)
    return (time.time() - start_time) * 1000  # returns time in milliseconds