def rec_ex(num:int)->None:
    if num > 0:
        print(num)    
        rec_ex(num-1)
    return

if __name__=='__main__':
    rec_ex(10)