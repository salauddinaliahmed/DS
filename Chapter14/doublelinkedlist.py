# Import linked list class or create a new extension.
class Node:
    def __init__(self, data) -> None:
        self.left = None
        self.right = None
        self.data = data


class DoubleLinkedList:
    def __init__(self, data=None) -> None:        
        self.first_node = Node(data)
        self.last_node = Node(data)

        # This logic links first and the last node.
        self.first_node.right = self.last_node
        self.last_node.left = self.first_node
    
    def __str__(self):
        current_node = self.first_node
        output = f"{self.first_node.data}, " if self.first_node.data else ''
        while current_node.right:
            current_node = current_node.right
            output += f'{str(current_node.data)}, '
        return output

    def print_reverse(self):
        current_node = self.last_node
        output = ''
        while current_node.left:
            output += str(current_node.data) + ', '
            current_node = current_node.left
        output += str(self.first_node.data)
        print (output)

    def insert(self, data):
        current_node = self.first_node
        if self.first_node.data == None:
            self.first_node.data = data
        else:
            while current_node.right:
                current_node = current_node.right

            if current_node.data == None:
                current_node.data = data
            else:
                new_node = Node(data)        
                new_node.left = current_node
                current_node.right = new_node
                self.last_node = new_node

    def insert_at_end(self, data):
        current_node = self.last_node
        new_node = Node(data)
        self.last_node.right = new_node
        new_node.left = self.last_node

        self.last_node = new_node

if __name__ == '__main__':
    dd = DoubleLinkedList()
    dd.insert(10)
    dd.insert(40)
    dd.insert(50)
    print(dd)
    dd.print_reverse()
    dd.insert_at_end(58)
    print(dd)