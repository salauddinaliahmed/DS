def selection_sort(array_list:list)->list:
    """
    Selection Sort:
    
    1. You set a flag to aid in swapping or not. Set it to false by default.
    2. The start index starts with 0.
    3. Create a while loop to loop until our start_index value is == the length of the array (Indicating we've reached the end of the array)
       - Here we initialise a index_val (or lower value) to whatever value which is at start index.
    4. Inside the while loop, we need to go through the whole array list again and compare with the first elem (start index) to see if we encounter any value
       is smaller than the value at our index_val. (We use a different variable here since we store the index of the value which is smaller than the first value here.)
    5. If we encounter something smaller than the value at the first index, we store the index value of the interger value. We set the do_sort flag to true to indicate
       that we now have a value to swap.
    6. Then we swap the index sorted with the start index.
    7. At the end of each for loop, we find each smallest value and we place it at the beginning of the array.
    8. We keep moving the starting point of the array since the previous for loop finishes placing the smallest value at the previous start_index.

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
    while start_index < len(array_list):
        do_sort = False
        index_val = start_index

        for _ in range(start_index, len(array_list)):
            # Do your loops
            if array_list[index_val] > array_list[_]:
                index_val = _
                do_sort = True
            
        if do_sort:
            array_list[start_index], array_list[index_val] = array_list[index_val], array_list[start_index]
        
        start_index += 1

    return array_list

if __name__ == '__main__':
    a = selection_sort([4, 3, 1, 5, 0, 2])
    print(a)