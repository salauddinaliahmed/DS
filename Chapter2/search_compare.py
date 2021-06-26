"""
For this exercise, we will compare the running time for a 
1. linear search,
2. Binary search and 
3. Recursive binary search.
"""

from time import time
import timeit

def linear_search(elem_list:list, search_for:int):
    start = timeit.default_timer()
    found = False
    for ind, each_elem in enumerate(elem_list):
        if each_elem == search_for:
            print(f"Found at index: {ind}")
            found = True
            break
    if found:
        print(f"Element found at index: {ind}")

    time_elapsed = timeit.default_timer() - start
    print(f"Time elapsed: {time_elapsed}")
    
    
if __name__ == '__main__':
    linear_search([x for x in range(10000)], 9999)
