class Node:
    def __init__(self, data=None) -> None:
        self.data = None
        self.next_node = None
        if data != None:
            self.data = data

class LinkedList:
    def __init__(self, data=None) -> None:
        self.first_node = Node(data)
    

    def __str__(self) -> str:
        current_node = self.first_node
        output = ''
        count = 0
        while current_node:
            output += str(count) + ' : ' + str(current_node.data) + ', '
            current_node = current_node.next_node
            count += 1
        return output

    def _goto_node(self, ind):
        current_index = 0
        current_node = self.first_node
        while current_index < ind:
            if current_node.next_node:
                current_node = current_node.next_node
            else:
                print("No node at that index.")
                return False
            current_index += 1
        return current_node

    # insert method
    def insert(self, val, ind=0, last=False):
        # If the first node is empty and there is no next node. 
        if self.first_node.data == None and self.first_node.next_node == None:
            self.first_node.data = val
            return

        if last:
            current_node = self.first_node
            while current_node:
                previous_node = current_node
                current_node = current_node.next_node
            previous_node.next_node = Node(val)
            return

        if ind == 0:
            current_node = self.first_node
            self.first_node = Node(val)
            self.first_node.next_node=current_node
            return 

        # Check if index was provided.
        if ind:
            previous_node = self._goto_node(ind-1)
            new_node = Node(val)
            new_next_node = previous_node.next_node
            new_node.next_node = new_next_node
            previous_node.next_node = new_node
            return
        


    # Read at index:
    def read(self, ind):
        return self._goto_node(ind)

    # Search
    def search(self, val):
        index = 0
        if val == self.first_node.data:
            return index
        current_node = self.first_node.next_node

        while current_node:
            index += 1
            if current_node.data == val:                
                return index
            current_node = current_node.next_node
        print("Element not found.")

    def delete(self, ind):
        print(f"Index to delete: {ind}")
        prev_node = self._goto_node(ind-1)
        delete_node = prev_node.next_node
        print(f"Delete node data: {delete_node.data}")
        next_node = prev_node.next_node.next_node

        prev_node.next_node = next_node
        delete_node.next_node = None


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert(1)
    for _ in range(5):
        ll.insert(_, last=True)
    print(ll)
    ll.insert(5, 2)
    print(ll)
    ll.delete(1)
    print("After delete")
    print(ll)
    print("Search...")
    print(ll.search(4))