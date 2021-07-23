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


def q3_triangular_nos(n):
    if n == 1:
        return 1
    return n + q3_triangular_nos(n-1)

def q4_index_x(s, count=0):
    if len(s) == 0: 
        return None
    
    if s[0] == 'x':
        return count
    return q4_index_x(s[1:], count=count+1) 

def q4_book_index(s):
    if s[0] == 'x':
        return 0
    return q4_book_index(s[1:]) + 1


if __name__ == '__main__':
    # print(q1_count_elems(['a', 'av', 'asd']))
    # print(q2_even_nos([0, 1, 2, 3, 4, 6]))
    print(q3_triangular_nos(7))
    print(q4_index_x('sst'))
    print(q4_book_index('abcdefghijklmnopqrstuvwxyz'))