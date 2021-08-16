"""Learning binary trees."""

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

class BinaryTree:
    def __init__(self, data) -> None:
        self.root = TreeNode(data)

    def _do_insert(data, node):
        if node == None:
            node = TreeNode(data)
        else:
            BinaryTree._do_insert(data, node.left)
            BinaryTree._do_insert(data, node.right)


    def insert(self, data):
        if self.root.data == None:
            self.root.data = data
            return
        else:
            BinaryTree._do_insert(data, self.root)   

    def __str__(self) -> str:
        return f"{self.root.data}, L:{self.root.left.data},R:{self.root.right}"



if __name__ == '__main__':
    t = BinaryTree(12)
    t.insert(54)
    # Pending search
    print(t)

