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
    global count
    count += 1
    print(count)
    if len(a) == 0:
        return 0
    
    if (a[0] + book_q1(a[1:])) > 100:
        return book_q1(a[1:])
    
    else:
        return a[0] + book_q1(a[1:])


if __name__ == '__main__':
    l = [20, 75, 30, 10]
    print(q1_unwanted_calls(l))
    print(book_q1(l))