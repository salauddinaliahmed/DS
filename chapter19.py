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
"""


if __name__ == '__main__':
    rev_string([1, 4, 5, 2])
