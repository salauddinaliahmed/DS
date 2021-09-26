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


if __name__ == '__main__':
    rev_string([1, 4, 5, 2])
    print(greedy_search([1,2, 5, 3]))
