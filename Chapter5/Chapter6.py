# Insertion sort.
from time import time
import timeit

def timer(foo):
    def _inner(*args, **kwargs):
        start_time = timeit.default_timer()
        x = foo(*args, **kwargs)
        print(f"Time taken for execution by {foo.__name__}: {timeit.default_timer() - start_time}")
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

@timer
def book_insertion(arr: list) -> list:
    print("Before sorting", arr)
    for i in range(1, len(arr)):
        temp_value = arr[i]
        # Start from the left value
        position = i - 1
        
        while position >= 0:
            if arr[position] > temp_value:
                arr[position+1] = arr[position]
                # Since we need to move left.
                position -= 1
            else:
                break

        # Now, we need to place back our temp value into empty position.
        # We do a position+1 here since 
        arr[position+1] = temp_value
    return arr

if __name__ == '__main__':
    import random
    l = [random.randint(0,500) for _ in range(50)]
    t = l.copy()
    print(f"Initial array: {l}")

    book_sort = book_insertion(l)
    sorted_array = insertion_sort(t)

    validation_array = sorted(l)
    print('------------------')
    print(f'Validation: {validation_array == sorted_array == book_sort}')
