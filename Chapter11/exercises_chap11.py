def q1_count_elems(a):
    if len(a) == 1:
        return len(a[0])
    return len(a[0]) + q1_count_elems(a[1:])
count = 0
def q2_even_nos(n, even_arr=[]):
    global count
    count = count+1
    print(count)
    if len(n) == 0:
        return even_arr
    else:
        if n[0] % 2 == 0:
            even_arr.append(n[0])
        return q2_even_nos(n[1:], even_arr=even_arr)


if __name__ == '__main__':
    print(q1_count_elems(['a', 'av', 'asd']))
    print(q2_even_nos([0, 1, 2, 3, 4, 6]))
