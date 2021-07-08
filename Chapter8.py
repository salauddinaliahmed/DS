# Hash Tables. Exercise

# 1. 
def inter_section(arr1, arr2)->list:
    arr3 = []
    hash_dict = dict()
    if len(arr1)>len(arr2):
        larger_arr = arr1
        smaller_arr = arr2
    else:
        larger_arr = arr2
        smaller_arr = arr1

    # Create the hash table/dictionary
    for _ in larger_arr:
        hash_dict[_] = True

    for _ in smaller_arr:
        if hash_dict.get(_, False):
            arr3.append(_)

    return arr3


# 2. 
def find_duplicate(arr)->str:
    hash_d = dict()

    # Returns first duplicate.
    for _ in arr:
        does_not_exist = hash_d.get(_, 0)
        if does_not_exist == 0:
            hash_d[_] = 1
        else:
            return _


#3. 
def one_alpha(s)-> str:
    alphs = [chr(_) for _ in range(97, 123)]
    s = s.lower().replace(' ', '')

    dic = {}
    for _ in s:
        x = dic.get(_, 5)
        if x == 5:
            dic[_] = True

    not_present = ''
    for _ in alphs:
        if dic.get(_, 10) == 10:
            not_present = _

    return not_present


# 4. 
def non_dup(s)-> str:
    d = dict()
    for _ in s:
        if d.get(_, False):
            d[_] += 1
        else:
            d[_] = 1

    for _ in s:
        if d[_] == 1:
            return _


if __name__ == "__main__":
    print(inter_section([1, 3, 4, 5, 6, 7], [0, 5, 4]))
    print(find_duplicate(['a', 'b', 'c', 'c']))
    print(one_alpha('the quick brown box jumps over a lazy dog'))
    print(non_dup('minimum'))