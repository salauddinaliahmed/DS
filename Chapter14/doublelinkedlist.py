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
    
    def __str__(self):
        current_node = self.first_node
        output = f"{self.first_node.data}, " if self.first_node.data else ''
        while current_node.right:
            current_node = current_node.right
            output += f'{str(current_node.data)}, '
        return output

    def print_reverse(self):
        current_node = self.first_node
        pass

    def insert(self, data):
        current_node = self.first_node
        new_node = Node(data)
        while current_node.right:
            current_node = current_node.right
        
        new_node.left = current_node
        current_node.right = new_node


if __name__ == '__main__':
    dd = DoubleLinkedList()
    print(dd)
    dd.insert(10)
    dd.insert(40)
    dd.insert(50)
    print(dd)
    