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


if __name__ == '__main__':
    print(bad_recursion_max([1, 2, 3, 4]))
    print("_"*10)
    print(better_recursion_max([1,5,3,4]))
