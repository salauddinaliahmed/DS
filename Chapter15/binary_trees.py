"""Learning binary trees."""

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.right_child = None
        self.left_child = None

class BinaryTree:
    def __init__(self, data) -> None:
        self.root = TreeNode(data)

    def insert(self, data):
        current_node = self.root
        if current_node.left_child == None:
            current_node.left_child = TreeNode(data)
        elif current_node.right_child == None:
            current_node.right_child = TreeNode(data)
            
    def __str__(self) -> str:
        return f"{self.root.data}, L:{self.root.left_child.data},R:{self.root.right_child}"



if __name__ == '__main__':
    t = BinaryTree(12)
    t.insert(54)
    # Pending search
    print(t)

