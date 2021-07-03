# Insertion sort.
from time import time
import timeit

def timer(foo):
    def _inner(*args, **kwargs):
        start_time = timeit.default_timer()
        x = foo(*args, **kwargs)
        print(f"Time taken for execution: {timeit.default_timer() - start_time}")
        return x
    return _inner

@timer
def insertion_sort(arr: list) -> list:

    for ind in range(1, len(arr)):
        for look_left in range(ind-1, -1, -1):
            l = arr[look_left]
            inv = arr[ind]
            if arr[look_left] > arr[ind]:
                arr[ind], arr[look_left] = arr[look_left], arr[ind]
                ind = look_left
            else:
                break

    return arr


if __name__ == '__main__':
    import random
    l = [random.randint(0,500) for _ in range(50)]
    l = [15, 1, 0, -1, 13]
    print(f"Initial array: {l}")

    sorted_array = insertion_sort(l)
    print(sorted_array)

    print('------------------')
    print(f'Validation: {sorted(l) == sorted_array}')
