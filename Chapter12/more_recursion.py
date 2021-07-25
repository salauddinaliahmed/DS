count = 0
def bad_recursion_max(l):
    global count
    count += 1
    print(count)
    if len(l) == 1:
        return l[0]

    if l[0] > bad_recursion_max(l[1:]):
        return l[0]
    
    else:
        return bad_recursion_max(l[1:])

def better_recursion_max(l):
    if len(l) == 1:
        return l[0]

    max_item = better_recursion_max(l[1:])
    
    if l[0] > max_item:
        return l[0]
    
    else:
        return max_item

def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n-2) + fib(n-1)

def fib_with_memo(n, memo=dict()):
    if n <= 1:
        return n
    
    if not memo.get(n):
        memo[n] = fib_with_memo(n-2, memo) + fib_with_memo(n-1, memo)

    return memo[n]


def fib_loop(n):
    i = 0
    for _ in range(n+1):
        i += _
    
    return i

if __name__ == '__main__':
    print(bad_recursion_max([1, 2, 3, 4]))
    print("_"*10)
    print(better_recursion_max([1,5,3,4]))
    print(fib(10))
    print('_'*5)
    print(fib_with_memo(10, {}))
    print("Iterative: ", fib_loop(10))