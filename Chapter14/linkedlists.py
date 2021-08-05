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

    # insert method
    def insert(self, val, ind=0):
        current_node = self.first_node
        current_index = 0
        if not ind:
            while current_node.next_node:
                current_node = current_node.next_node
            current_node.next_node = Node(val)
        
        else:
            while current_index <= ind-1:
                if current_node.next_node:
                    current_index += 1
                    current_node = current_node.next_node
                else:
                    print("No node at that index.")
                    return

            next_node = current_node.next_node
            new_node = Node(val)

            current_node.next_node = new_node
            new_node.next_node = next_node
        

    # Read at index:
    def read(self, ind):
        current_index = 0
        current_node = self.first_node
        while current_index <= ind:
            current_index += 1
            current_node = current_node.next_node
        
        if current_node.data:
            return current_node.data
        
        else:
            print("No element at that index.")

    # Search
    def search(self, val):
        pass

    def delete(self, ind):
        pass


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert(1)
    for _ in range(5):
        ll.insert(_)
    print(ll)
    ll.insert(5, 2)
    print(ll)