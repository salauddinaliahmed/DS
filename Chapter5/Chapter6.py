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
    """
    Insertion sort, you start with the index 1, pick the value up from the array,
    compare it with whatever is on the left side of the picked index,
    If the value is greater than the value at picked index, we move the value to the right. (Basically shift right, or place it in the value of picked index)
    If the value is lower, we break the pass through and increment the index by 1, so on until we reach the end of the array.

    Eg: [1, 4, 2, 3]

    Index 1 picked.
        4
    [1,  , 2, 3]
     |
    Compare with left. (4>1, so we end the first walk through)
    Index 2 picked
            2
    [ 1, 4,  , 3]
         |
         We look left.
    2 > 4, False, here we encountered a value greater than the index value so we move it right.
        2
    [1,   ,4, 3] 
    We then compare 2 with 1, since 2 is greater we end the pass through. We place 2 in the empty slot
    Then we look at index 3
          4  
    [1, 2,  , 3]
    We look left, 4 > 2, so we end this pass through.
    Index 3
              3
    [1, 2, 4,  ]
    We look left, 3>4, False, so we move 4 to the right.
    
           3
    [1, 2,  , 4]
    Then we check 3 with 2, Since 3 is greater than 2, we place 3 down in the empty slot.
    Now we have walked through the whole list and its sorted.
    [1, 2, 3, 4]
    """
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
    
    
"""
Exercise 6:
1. Algo takes 3N^2 + 2N + 1 -> O(n^2)
2. N + logN -> O(N)
3. Summing up to 10 from 2 lists: Best Case: O(1) ; Worst Case: O(N^2); Average Case: O(N^2/2)
4. Find if a string contains capital x, We dont need to look further if we encounter it once.
    - With the below implementation: 
        Worst Case: O(N)
        Best Case: O(1)
        Average Case: O(N/2)
"""
def findX(string: str) ->bool:
    for _ in string:
        if _ == 'X':
            return True
    return False