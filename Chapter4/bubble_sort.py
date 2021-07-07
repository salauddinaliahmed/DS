def bubble_sort(seq: list, seq_length, index:int = 0):
    if seq_length <= 1:
        return seq
    first = seq[index]
    second = seq[index+1]
    if first > second:
        seq[index], seq[index+1] = seq[index+1], seq[index]

    if len(seq) - 1 == index+1:
        seq_length -= 1
        index = -1

    return bubble_sort(seq, seq_length=seq_length, index=index+1)

# Linear method shown in the book.
def better_bubble_sort(seq):
    """
    In bubble sort we compare 
    [4, 2, 3, 1]
     |  |
     then we swap, if we find that value at index[0] > index[1]
    [2, 4, 3, 1]
        |  | 
     then we compare 4 with 3, 4 > 3,  we swap again
    [2, 3, 4, 1]
           |  |
     then we swap 4 and 1, 
    [2, 3, 1, 4]
    By the end of the first pass through, the max value bubbles up to the right side of the array.
    Then we can reduce the array size by 1. only using the array [2, 3, 1]
    [2, 1, 3]
    [1, 2, 3]
    We break, when we do not have any more swaps form a walk through.
    
    """
    last_index = len(seq) - 1
    sorted = False

    while not sorted:
        # Set this to True incase the list does not need any swaps,
        # This value will remain true.
        sorted = True

        for ind in range(last_index):
            if seq[ind] > seq[ind+1]:
                # Swap
                seq[ind], seq[ind+1] = seq[ind+1], seq[ind]
                sorted = False
        
        # Once one pass of the entire list is done, the largest element
        # Bubbles up. Thus, use n-1.
        last_index = last_index - 1
    return seq


if __name__=='__main__':
    import random
    # My recursive algorithms are highly inefficient, they do not work for small numbers.

    unsorted_list = [random.randint(0,1000) for _ in range(25)]
    sorted_list = bubble_sort(unsorted_list, len(unsorted_list))
    print(sorted_list)

    print("Better version:----------------")
    better_sorted_list = better_bubble_sort(unsorted_list)
    print(better_sorted_list)

    print(f"Validation: {sorted_list == better_sorted_list}")
    # O(n^2) is called quadratic.