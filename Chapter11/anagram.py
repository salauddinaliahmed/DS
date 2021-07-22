def anagram(s):
    # Base case.
    if len(s) == 1:
        return s

    all_anagrams = []
    remaning_anagrams = anagram(s[1:])

    for each_a in remaning_anagrams:
        for each_index in range(len(each_a)+1):
            _ = list(each_a)
            _.insert(each_index, s[0])
            all_anagrams.append(''.join(_))

    return all_anagrams

if __name__ == '__main__':
    word = 'abcd'
    print(anagram(word))
