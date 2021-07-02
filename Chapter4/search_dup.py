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
        
# Chapter 4, exercise question 4, O(n) solution.
def greatest_number(seq: list) -> bool:
    greatest_value = 0
    for _ in seq:
        if _ > greatest_value:
            greatest_value = _
    
    print(f"Greatest Value: {greatest_value}")

if __name__ == '__main__':
    search_dup([1, 2, 3, 4, 5, 132])
    greatest_number([1, 2, 3, 4, 774, 132])