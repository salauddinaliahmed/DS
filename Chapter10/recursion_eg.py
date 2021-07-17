def rec_ex(num:int)->None:
    if num > 0:
        print(num)    
        rec_ex(num-1)
    return


def fact(num:int)->None:
    if num <= 1:
        return 1
    return num * fact(num-1)


if __name__=='__main__':
    #rec_ex(10)
    x = fact(5)
    print(x)