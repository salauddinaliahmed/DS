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
        while ind_last > 0 and self.heap_arr[self.parent_of(ind_last)] < self.heap_arr[ind_last]:
            # Compare with the parent, if greater, swap. (Trickle up)
            a = self.heap_arr[self.parent_of(ind_last)]
            b = self.heap_arr[ind_last]

            self.heap_arr[self.parent_of(ind_last)], self.heap_arr[ind_last] = self.heap_arr[ind_last], self.heap_arr[self.parent_of(ind_last)]
            ind_last = self.parent_of(ind_last)
            

    def delete(self):
        """Only deletes the root node."""
        pass


if __name__ == '__main__':
    h = Heap(10)
    h.insert(4)
    h.insert(15)
    print(h)