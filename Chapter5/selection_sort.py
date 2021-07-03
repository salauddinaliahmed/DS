def selection_sort(array_list:list)->list:
    """
    Selection Sort:
    Theory:
    You compare all the values of the array with the first value, storing the index of any value which is smaller than our first value. 
    If we find such value, we swap it with the first value.
    So, since we walked though the whole array, we know that we found the smallest value in that array. Moving it at the start position means, its placed in the right spot.
    We need to find the next smallest value, so we can increment our next walk from value 2 of the array.
    and so on until we reach the last value in the array, by then the entire array is sorted.

    eg: 
        [3, 4, 2, 1]
         |
        store 3 as lowest value, compare with all the other elements.
        After first plass of the array, we find that the lowest value is 1 so we swap it with the starting point 3
        [1, 4, 2, 3]
            |
        Now that we know 1 is in the right spot, we change the start index to the next value which is 4, we find 2 to be the lowest in this pass
        So, we swap it with the start index 
        [1, 2, 4, 3]
               |
        Then, we repeat the process and we swap 4 and 3 and we've reached the end of the list.


    Time Complexity - O(n^2) Quadratic

    """
    start_index = 0
        # while start_index < len(array_list):
        #     do_sort = False
        #     index_val = start_index

    for start_index in range(0, len(array_list)-1):
        lowest_val_index = start_index
        for _ in range(start_index, len(array_list)):
            # Do your loops
            if array_list[lowest_val_index] > array_list[_]:
                lowest_val_index = _            
        
        if start_index != lowest_val_index:
            array_list[start_index], array_list[lowest_val_index] = array_list[lowest_val_index], array_list[start_index]

    return array_list

if __name__ == '__main__':
    a = selection_sort([4, 3, 1, 5, 0, 2, -1])
    print(a)

"""
Exercise:

1. 4n + 16 -> O(n)
2. 2n^2 -> O(n^2)
3. 2n -> O(n)
4. 3n -> O(n^3)
5. n/2 -> O(n^3)
6. n*(n/2) -> O(n^2)

"""