from functools import lru_cache

def q1_unwanted_calls(a):
    if len(a) == 0:
        return 0

    accumulated_sum = q1_unwanted_calls(a[1:])

    if a[0] + accumulated_sum > 100:
        return accumulated_sum 

    else:
        return a[0] + accumulated_sum

count = 0
def book_q1(a):
    if len(a) == 0:
        return 0
    
    if (a[0] + book_q1(a[1:])) > 100:
        return book_q1(a[1:])
    
    else:
        return a[0] + book_q1(a[1:])


# @lru_cache
def q2_memo_golomb(n):
    if n == 1:
        return 1
    
    return 1 + q2_memo_golomb(n - q2_memo_golomb(q2_memo_golomb(n-1)))


def q2_man_memo(n, d=dict()):

    if n == 1 and not d.get(n, False):
        d[n] = 1
        return d[n]
    
    
    if not d.get(n, False):
        d[n] = 1 + q2_man_memo(n - q2_man_memo(q2_man_memo(n-1, d=d), d=d), d=d)

    return d[n]

count=0
@lru_cache
def q3_unique_paths(rows, columns):
    global count
    count += 1
    if rows == 1 or columns == 1:
        return 1

    return q3_unique_paths(rows-1, columns) + q3_unique_paths(rows, columns-1)

new_count=0
def q3_unique_paths_new(rows, columns, memo_dict={}):
    global new_count
    new_count += 1
    """Dictionary can work even with tuples as keys."""
    if rows == 1 or columns == 1:
        return 1
    
    if not memo_dict.get((rows,columns), False):
        memo_dict[rows, columns] = q3_unique_paths_new(rows-1, columns, memo_dict=memo_dict) + q3_unique_paths_new(rows, columns-1, memo_dict=memo_dict)

    return memo_dict[rows,columns]



if __name__ == '__main__':
    l = [20, 75, 30, 10]
    print(q1_unwanted_calls(l))
    print(book_q1(l))
    print(q2_memo_golomb(10))
    print(q2_man_memo(4))

    print("---------------")
    print(q3_unique_paths(3,3))
    
    print("---------------")
    print(q3_unique_paths_new(3,3))

    print(f"Count is: {count}")
    print(f"Not Lru: {new_count}")