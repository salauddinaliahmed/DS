def search_dup(seq:list) -> bool:
    existing_list = [0 for _ in range(max(seq)+1)]
    for i in seq:
        if existing_list[i] == 1:
            print("Has duplicate")
            return True
        else:
            existing_list[i] = 1
    print("No duplicates")
    return False
        

if __name__ == '__main__':
    search_dup([1, 2, 3, 4, 5, 132])