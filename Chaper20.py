def temp_sort(arr):
    """
    Sorts temperatures ranging exclusively from 97 to 99.
    """
    result = []
    given_temp_dict = {}
    for each_temp in arr:
        if not given_temp_dict.get(each_temp, False):
            given_temp_dict[each_temp] = 1
        else:
            given_temp_dict[each_temp] += 1

    
    start_temp = 97.0
    sorted_list = []
    while start_temp < 99.0:
        start_temp += 0.1
        start_temp = round(start_temp, 2)
        sorted_list.append(start_temp)

    for each_temp in sorted_list:
        if x:=given_temp_dict.get(each_temp, False):
            for _ in range(x):
                result.append(each_temp)

    return result

def longest_sequence(arr):

    """
    Should loop through the array and find the longest sequence. 
    
    1. Create a dictionary and then store the values.
    2. Loop through each number and check if the next subsequent number is in the dictionary.
        - If it is, then increase count by one (Loop through incrementing one each time until you dont find it)
        - Keep track of the count, if its great next time you update. 
    """
    longest_sequence = 0
    new_dict = {}
    max_number = 0 
    min_number = float('inf')

    for _ in arr:
        if _ > max_number:
            max_number = _
        elif _ < min_number:
            min_number = _

    for i in range(min_number, max_number+1):
        new_dict[i] = 6

    for _ in arr:
        if new_dict.get(_):
            new_dict[_] = 1

    new_dict_sorted = []
    for each_key, each_val in new_dict.items():
        if each_val == 1:
            new_dict_sorted.append(each_key)

    start_val = new_dict_sorted[0]
    max_l = len(new_dict_sorted)
    i = 1
    current_longest_seq = 1
    while i < max_l:
        if new_dict_sorted[i] == start_val + 1:
            current_longest_seq += 1
        else:
            if current_longest_seq > longest_sequence:
                longest_sequence = current_longest_seq
            current_longest_seq = 1
        
        start_val = new_dict_sorted[i]
        i += 1

    print("Current_Longest_sequence: ", longest_sequence)
    print(new_dict_sorted)


def new_lng_seq(arr):
    new_dict = {}
    longest_sq = 0

    for i in arr:
        new_dict[i]=True

    for e in arr:
        # A number lower than this does not exist.
        if not new_dict.get(e-1, False):
            current_sequence = 1 
            current_number = e

            while new_dict.get(current_number+1, False):
                current_sequence += 1
                current_number += 1


            if current_sequence > longest_sq:
                longest_sq = current_sequence
    
    print(f"New logic: {longest_sq}")
    return longest_sq



        


if __name__ == '__main__':
    # print(temp_sort([98.6, 98.0, 99.0, 98.9, 95.5, 98.2, 98.0, 97.1]))
    # What i missed in the earlier implementation is that my algo does not respect duplicates.
    longest_sequence([13, 54, 50, 12, 14, 115])
    new_lng_seq([13, 54, 50, 12, 14, 115])
