def selection_sort(array_list:list)->list:
    """
    You start with the list : [3, 4, 2, 1]

    - start index = 0 
    val index = 0, start_val = 3
    - from index to len(list) - loop though and compare with start_val, if we find something less than start val, then we replace start val
    with the value at that index with the value at val index.

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