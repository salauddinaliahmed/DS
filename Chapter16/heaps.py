"Heaps:"

class Heap:
    def __init__(self, root) -> None:
        # We will keep an array.
        # We assume 0 based indexes.
        self.heap_arr = [root]
    
    @property
    def first_node(self):
        return self.heap_arr[0]

    def __str__(self) -> str:
        return f'The heap: {self.heap_arr}'
    
    @property
    def last_node(self):
        return self.heap_arr[-1]
    
    def parent_of(self, index):
        return (index-1)//2
    
    def left_child_of(self, index):
        return (index*2)+1
    
    def right_child_of(self, index):
        return (index*2)+2

    def insert(self, val):
        # Insert value at the end of the tree (really an array)
        self.heap_arr.append(val)

        ind_last = len(self.heap_arr) - 1

        # Combined 2 conditions rather than using break with if and else.
        x = self.heap_arr[self.parent_of(ind_last)]
        y = self.heap_arr[ind_last]
        while ind_last > 0 and self.heap_arr[self.parent_of(ind_last)] > self.heap_arr[ind_last]:
            # Compare with the parent, if greater, swap. (Trickle up)
            a = self.heap_arr[self.parent_of(ind_last)]
            b = self.heap_arr[ind_last]

            self.heap_arr[self.parent_of(ind_last)], self.heap_arr[ind_last] = self.heap_arr[ind_last], self.heap_arr[self.parent_of(ind_last)]
            ind_last = self.parent_of(ind_last)


    def greatest_sibling(self, ind):
        left = (ind*2) + 1
        right = (ind*2) + 2
        max_len = len(self.heap_arr)

        #  and left <= max_len part unnecessary.
        if right > max_len:
            return left

        else:
            if self.heap_arr[right] < self.heap_arr[left]:
                return right
            else:
                return left

    def has_greater_child(self, ind):
        left = self.left_child_of(ind)
        right = self.right_child_of(ind)
        
        # Because we are indexing, we need to check if we have an indexable value.
        max_len = len(self.heap_arr) - 1

        if right > max_len:
            if left > max_len:
                return False
            else:
                return self.heap_arr[left] < self.heap_arr[ind]

        else:
            return self.heap_arr[left] < self.heap_arr[ind] or self.heap_arr[right] < self.heap_arr[ind]


    def delete(self):
        """Only deletes the root node."""
        root_node = self.first_node
        # Pop defaults to last value. Delete the last value.
        self.heap_arr[0] = self.heap_arr.pop()

        print(f"Heap after delete: {self.heap_arr}")
        current_node = 0

        while current_node < len(self.heap_arr) and self.has_greater_child(current_node):
            
            gc = self.greatest_sibling(current_node)
            self.heap_arr[current_node], self.heap_arr[gc] = self.heap_arr[gc], self.heap_arr[current_node]
            current_node = gc
    
        return root_node






        


if __name__ == '__main__':
    h = Heap(10)
    h.insert(4)
    h.insert(7)
    h.insert(15)
    print(h)
    print(h.delete())
    print(h)