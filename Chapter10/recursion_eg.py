def rec_ex(num:int)->None:
    if num > 0:
        print(num)    
        rec_ex(num-1)
    return


def fact(num:int)->None:
    if num <= 1:
        return 1
    return num * fact(num-1)


def dir_parser(dirs)->None:
    """Write a function that parses through the directories at arbitrary levels (recursive)"""
    pass


def only_numbers(arr)->None:
    if isinstance(arr, int):
        print(arr)
        return

    for each_item in arr:    
        only_numbers(each_item)


def better_only_numbers(arr)-> None:
    for each_item in arr:
        if isinstance(each_item, list):
            better_only_numbers(each_item)
        else:
            print(each_item)



def summ(low, high):
    if high <= low:
        return 1
    return high + summ(low, high-1)


def arr_doubler(arr, i=0)-> list:
    if i == len(arr):
        return
    arr[i] *= 2
    arr_doubler(arr, i=i+1)

# Factorial top down
def fact(n, i=1, product=1):
    if i > n:
        return product
    return fact(n, i+1, product=product * i)

def arr_sum(arr):
    if len(arr) == 0:
        return 0
    return arr[-1] + arr_sum(arr[:-1])

def str_rev(st):
    if len(st)==1:
        return st[0]
    return st[-1] + str_rev(st[0:-1])

if __name__=='__main__':
    dirs = ['a', ['b', 'c'], 'e', ['f', 'g']]
    #rec_ex(10)
    # x = fact(5)
    # print(x)
    # y = summ(1, 10)
    # print(y)
    # ar = [1, 2, [3, 4, 5], [6, 4, [3, 2, 2, [1, 4, 4, 7], [2, 66, 6, 9, [1, 3]]]], 3]
    # only_numbers(ar)
    # print('_'*10)
    # better_only_numbers(ar)
    arr = [1, 2, 3, 4, 5]
    arr_doubler(arr)
    print(arr)
    t = fact(5)
    print(t)
    print("-"*10)
    tar = [1, 2, 3, 4, 5]
    t = arr_sum(tar)
    print(t)
    vol = "badday"
    print(str_rev(vol))