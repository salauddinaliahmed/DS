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
        # We do a position+1 here since position starts with left (or looks/compares one left)
        # If we moved any element to the right, or not, there will always be one open space after position.
        # Due to the movement or just selection
        """
        Example:
            p - Position 
                  3
            1.[1,   , 2, 4]
               |
               p
            Empty space at position + 1.

                     3
            2. [1, 5,  , 4]
                   |
                   p
                We compare 3 with 5, since 5 is greater we move 5.
                3 - is hanging up
                [1,  , 5, 4]
                 |
                 p (one left since we already compared 5). Observe here that the free space is always on the right side of the position.
                 This is inately because we are moving right and comparing left. 
                 
                position is now
             
        """
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
    
    
