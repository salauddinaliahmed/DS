import Stacks

def palindrome(word) -> bool:
    s = Stacks.Stack()
    for _ in word:
        s.push(_)
    
    rev_word = ''
    for _ in range(len(word)):
        rev_word += s.pop()

    return rev_word == word


def string_reverse(word):
    if len(word) == 1:
        return word

    revered_string = string_reverse(word[1:]) + word[0]
    return revered_string


if __name__ == '__main__':
    # print(palindrome('boob'))
    # print(palindrome('lafor'))
    print(string_reverse('lafor'))