from Chapter11.anagram import anagram


def rev_string(s):
    """
    Reversing the string in O(1) Space
    """
    for i in range(len(s)//2):
        s[i], s[len(s)-1-i] = s[len(s)-1-i], s[i]

    print (s)
# Read about the framework to use for optimizing an algorithm.
"""
1. Check the current complexity / performance of the algo.
2. Come up with the best logically possible complexity.
3. Incase the best complexity is better than the current complexity. 
    Try to get the algo either to the best estimate or something between the best estimate or the current estimate.

4. Read about looking at the algo and pondering if the act of constant time retrieval (through a hash table) would speed up the algo.
5. Read about greedy approach where the currently available option is selected as the best option.
   for eg: When finding the greatest value in an array, you could sort it and then return greatest elem (nLogn) or you could make the first 
   element as the greatest and iterate through the array once, and swap the greatest value if we encounter a value greater than the earlier value.

"""
def greedy_search(s):
    greatest_num = 0
    for each in s:
        if each > greatest_num:
            greatest_num = each
    return greatest_num


def greedy_find_max_subsection(l):
    current_score = 0
    greatest_score = 0

    for each_number in l:
        current_score += each_number
        
        if current_score <= 0:
            current_score = 0
        
        else:
            # greatest_score = current_score if greatest_score < current_score else greatest_score

            greatest_score = current_score
    
    return greatest_score

def stock_upward(l):
    mid_point = float('inf')
    low_point = l[0]
    for each_elem in l:
        if each_elem < low_point:
            low_point = each_elem
        elif each_elem < mid_point:
            mid_point = each_elem
        elif each_elem > mid_point:
            highest_point = each_elem
        
    if highest_point:
        print(f"Lowest: {low_point}, middle: {mid_point}, highest: {highest_point}")
        return True
    
## Chapter 20
def anagram_checker(first_word, second_word):
    first_word_dict = {}
    second_word_dict = {}

    for each_letter in first_word:
        if each_letter in first_word:
            if not first_word_dict.get(each_letter, False):
                first_word_dict[each_letter] = 1
            else:
                first_word_dict[each_letter] += 1


    for each_letter in second_word:
        if each_letter in second_word:
            if not second_word_dict.get(each_letter, False):
                second_word_dict[each_letter] = 1
            else:
                second_word_dict[each_letter] += 1

    return first_word_dict == second_word_dict


def athelete_check(arr1, arr2):
    ath_dict = {}
    multi_ath = []
    for each_dict in arr1:
        ath_dict[each_dict['first_name']+each_dict['last_name']] = True

    for each_dict in arr2:
        if ath_dict.get(each_dict['first_name']+each_dict['last_name'], False):
            multi_ath.append(f'{each_dict["first_name"]} {each_dict["last_name"]}')
    
    return multi_ath

def missing_no(arr):
    max_elem = max(arr)
    sum_to_n_terms = (max_elem * (max_elem + 1))/2
    current_sum = sum(arr)
    return int(sum_to_n_terms - current_sum)


def stock_profit(arr):
    """
    Main idea: You buy low and sell high. 
    Imp: The arr is in a series, you need to follow a sequence.
    1. Take the first value as the lowest_value.
    1.1 Make highest value 0
    2. Iterate through the list.
        2.1 See if the value is lower than the lowest_value.
            2.1.1 If true, replace the lowest_value. 
        2.2 See if the value is greater than the highest value.
            2.2.2 If true, replace the highest value.

    3. Once done with the entire iteration thought the arr, substract highest_value from lowest value to get the profit

    What i did: I had to reset the high price incase we find that the lowest price's index is higher than the highest price encountered.


    """
    
    # Think about a way to preserve order.
    lowest_val = highest_value = buy_price = sell_price = arr[0]
    previous_high_index = 0
    profit = highest_value - lowest_val

    for i, each_val in enumerate(arr):
        if each_val < lowest_val:
            if i >= previous_high_index:
                lowest_val = each_val
                highest_value = 0
        elif each_val > highest_value:
            previous_high_index = i
            highest_value = each_val

        if (x:=highest_value - lowest_val) > profit:
            buy_price = lowest_val
            sell_price = highest_value
            profit = x

    print(f"Profits: {profit} as stock was bought with price {buy_price} and sold at {sell_price}")

def question_4(*args, **kwargs):
    pass


if __name__ == '__main__':
    # rev_string([1, 4, 5, 2])
    # # print(greedy_search([1,2, 5, 3]))
    # # print(greedy_find_max_subsection([4, -4, -1, -3, -5, -9]))
    # # print(stock_upward([5, 2, 8, 4, 3, 7]))
    # # print(stock_upward([22, 25, 21, 18, 19.6, 17, 16, 20.5]))
    # print(anagram_checker('cinema', 'icemant'))
    # print(
    #     athelete_check(
    #         [{'first_name': 'Bob', 'last_name': 'Lang', 'team': 'lol'},
    #          {'first_name': 'Cassy', 'last_name':'Lang', 'team': 'Pony'}
    #         ],
    #         [
    #             {'first_name':'Cassy', 'last_name': 'Lang', 'team': 'Bottles'},
    #         ]
    #     )
    # )
    # print(missing_no([1,2,4,5]))

    stock_profit([10, 7, 5, 8, 11, 2, 6])
    stock_profit([9, 10, 5, 7, 2, 1])