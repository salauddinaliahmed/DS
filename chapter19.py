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



if __name__ == '__main__':
    rev_string([1, 4, 5, 2])
    # print(greedy_search([1,2, 5, 3]))
    # print(greedy_find_max_subsection([4, -4, -1, -3, -5, -9]))
    # print(stock_upward([5, 2, 8, 4, 3, 7]))
    # print(stock_upward([22, 25, 21, 18, 19.6, 17, 16, 20.5]))
    print(anagram_checker('cinema', 'icemant'))