# Implement bubble sort. 

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