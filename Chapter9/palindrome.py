import Stacks

def palindrome(word) -> bool:
    s = Stacks.Stack()
    for _ in word:
        s.push(_)
    
    rev_word = ''
    for _ in range(len(word)):
        rev_word += s.pop()

    return rev_word == word


if __name__ == '__main__':
    print(palindrome('boob'))
