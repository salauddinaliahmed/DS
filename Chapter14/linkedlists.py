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
        while current_node.next_node:
            current_node = current_node.next_node
            output += str(current_node.data) + ', '
        return output

    def _goto_node(self, ind):
        current_index = 0
        current_node = self.first_node
        while current_index <= ind:
            if current_node.next_node:
                current_index += 1
                current_node = current_node.next_node
            else:
                print("No node at that index.")
                return False
        return current_node


    # insert method
    def insert(self, val, ind=0):
        current_node = self.first_node
        current_index = 0
        if not ind:
            while current_node.next_node:
                current_node = current_node.next_node
            current_node.next_node = Node(val)
        
        else:
            current_node = self._goto_node(ind-1)

            next_node = current_node.next_node
            new_node = Node(val)

            current_node.next_node = new_node
            new_node.next_node = next_node
        

    # Read at index:
    def read(self, ind):
        return self._goto_node(ind)

    # Search
    def search(self, val):
        pass

    def delete(self, ind):
        prev_node = self._goto_node(ind-1)
        delete_node = prev_node.next_node
        next_node = prev_node.next_node.next_node

        prev_node.next_node = next_node
        delete_node.next_node = None


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert(1)
    for _ in range(5):
        ll.insert(_)
    print(ll)
    ll.insert(5, 2)
    print(ll)
    ll.delete(1)
    print("After delete")
    print(ll)