def q1_count_elems(a):
    if len(a) == 1:
        return len(a[0])
    return len(a[0]) + q1_count_elems(a[1:])



if __name__ == '__main__':
    print(q1_count_elems(['a', 'av', 'asd']))
