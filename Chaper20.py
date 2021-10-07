def temp_sort(arr):
    """
    Sorts temperatures ranging exclusively from 97 to 99.
    """
    result = []
    given_temp_dict = {}
    for each_temp in arr:
        if not given_temp_dict.get(each_temp, False):
            given_temp_dict[each_temp] = True

    
    start_temp = 97.0
    sorted_list = []
    while start_temp < 99.0:
        start_temp += 0.1
        start_temp = round(start_temp, 2)
        sorted_list.append(start_temp)

    for each_temp in sorted_list:
        if given_temp_dict.get(each_temp, False):
            result.append(each_temp)

    return result
    



if __name__ == '__main__':
    print(temp_sort([98.6, 98.0, 99.0, 98.9, 95.5, 98.2, 98.0, 97.1]))