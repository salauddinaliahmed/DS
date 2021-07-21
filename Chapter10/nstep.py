def n_step(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        return n_step(n-1) + n_step(n-2) + n_step(n-3)


if __name__ == '__main__':
    x = n_step(3)
    print(x)
