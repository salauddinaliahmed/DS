def largest_number(array):
    largest_product_sofar = array[0] * array[1] * array[2]
    i = 0 
    no_k = 0
    k_loo = 0
    while i < len(array):
        j = i + 1
        while j < len(array):
            k = j + 1
            k_loop = 0
            while k < len(array):
                if array[i] * array[j] * array[k] > largest_product_sofar:
                    largest_product_sofar = array[i] * array[j] * array[k]
                k += 1
                k_loop += 1
            if k_loop == 0:
                no_k+=1
            else:
                k_loo+=1
                
            j += 1
        i += 1
    # print (f" This is i: {i}\n This is j: {j}\n This is k: {k}\n")
    print(f"This is how many times k not looped: {no_k}")
    print(f"This is how many times k looped: {k_loo}")
    return largest_product_sofar

def foo(x):
    opt = 0
    for _ in range(x):
        s = _+1
        for j in range(s, x):
            opt+=1
        print(f"OPTL {opt} and x: {x}")
        opt = 0

if __name__=='__main__':
    # x = largest_number([1, 2, 3, 4, 5])
    # print(x)
    foo(10)