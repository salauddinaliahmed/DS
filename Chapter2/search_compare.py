"""
For this exercise, we will compare the running time for a 
1. linear search,
2. Binary search and 
3. Recursive binary search.
"""

import time

def linear_search(elem_list:list, search_for:int) -> None:
    start = time.time()
    found = False
    for ind, each_elem in enumerate(elem_list):
        if each_elem == search_for:
            print(f"Found at index: {ind}")
            found = True
            break
    if found:
        print(f"Element found at index: {ind}")

    time_elapsed = time.time() - start
    print(f"Time elapsed: {time_elapsed}")
    
    

if __name__ == '___main__':
    linear_search([1, 2, 3], 2)
