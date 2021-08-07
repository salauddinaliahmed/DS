# Import linked list class or create a new extension.
class Node:
    def __init__(self, data) -> None:
        self.left = None
        self.right = None
        self.data = data


class DoubleLinkedList:
    def __init__(self, data) -> None:        
        self.first_node = Node(data)
