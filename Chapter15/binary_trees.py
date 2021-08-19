"""Learning binary trees."""
x = [0, 1, 2, 3, 4, 5]
class TreeNode:
    def __init__(self, data=None):
        self.data = data
        self.right = None
        self.left = None

class BinaryTree:
    def __init__(self, data=None) -> None:
        self.root = TreeNode(data)

    @staticmethod
    def _do_insert(current_node, value):        
        if value > current_node.data:
            if current_node.right == None:
                current_node.right = TreeNode(value)
            else:
                BinaryTree._do_insert(current_node.right, value)
        else:
            if current_node.left == None:
                current_node.left = TreeNode(value)
            else:
                BinaryTree._do_insert(current_node.left, value)

        
    def insert(self, value):
        if self.root.data == None:
            self.root.data = value
            return
        BinaryTree._do_insert(self.root, value)

    @staticmethod
    def _nodes_printer(node, direction=None):
        if node == None:
            return
        
        print(f"{direction.upper() if direction else 'Root'}:{node.data}")
        BinaryTree._nodes_printer(node.left, direction='left')
        BinaryTree._nodes_printer(node.right, direction='right')


    def __str__(self) -> str:
        BinaryTree._nodes_printer(self.root)
        return ''       

    def _do_search(node, elem):
        if node == None or node.data == elem:
            return node

        # O(N) complexity. Useless but when combining recusive functions, we need to perform some sort of combination
        # to its return values. They can have a single return for obvious reasons.        
        # return BinaryTree._do_search(node.right, elem) or BinaryTree._do_search(node.left, elem)

        if elem > node.data:
            return BinaryTree._do_search(node.right, elem)
        else:
            return BinaryTree._do_search(node.left, elem)


    def _do_delete(node):
        if node.left != None and node.right == None:
            node.data = node.left.data
            node.left = None
        elif node.right != None and node.left == None:
            node.data = node.right.data
            node.right = None
        elif node.right == None and node.left == None:
            return node

        pass
    

    def delete(self, elem):
        pass

    @staticmethod
    def do_rec(im):
        if im == 0:
            return x.pop()
        t = BinaryTree.do_rec(im-1)
        return t

    def search(self, elem):
        return BinaryTree._do_search(self.root, elem)


if __name__ == '__main__':
    import random
    t = BinaryTree()
    e = [20, 45, 30, 72, 18]
    for _ in e:
        t.insert(_)

    # Pending search
    print(x.pop())
    print(x)
    print(t)
    # print(t.search(30).data)
    # print(t.do_rec(5))
