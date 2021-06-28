"""
For this exercise, we will compare the running time for a 
1. linear search,
2. Binary search and 
3. Recursive binary search.
"""

from time import time
import sys
import timeit


def timer_func(baz):
    def _inner(*args, **kwargs):
        time_before = timeit.default_timer()
        baz(*args, **kwargs)
        print(f"Total time taken by {baz.__name__} is: {timeit.default_timer()-time_before}")
        return
    return _inner


@timer_func
def linear_search(elem_list:list, search_for:int):
    found = False
    for ind, each_elem in enumerate(elem_list):
        if each_elem == search_for:
            found = True
            break
    if found:
        print(f"Element found at index: {ind}")


@timer_func
def binarysearch(*args, **kwargs):
    binary_search(*args, **kwargs)


def binary_search(element_list: list, search_item: int, start: int, end: int):
    if start < end:
        mid = (start + end ) // 2
        if element_list[mid] > search_item:
            end = mid - 1
        elif element_list[mid] < search_item:
            start = mid + 1
        else:
            print(f"Element found at: {mid}")
            return
        binary_search(element_list, search_item, start, end)
    

if __name__ == '__main__':
    sys.setrecursionlimit(10000)
    l = [x for x in range(10000)]
    linear_search(l, 9999)
    binarysearch(l, 9999, start=0, end=len(l)-1)
