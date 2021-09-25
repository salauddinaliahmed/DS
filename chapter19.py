def rev_string(s):
    """
    Reversing the string in O(1) Space
    """
    for i in range(len(s)//2):
        s[i], s[len(s)-1-i] = s[len(s)-1-i], s[i]

    print (s)


if __name__ == '__main__':
    rev_string([1, 4, 5, 2])
