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
    def _do_delete(node, n_val):
        # First the base case.
        if node == None:
            return None
        
        # Then we need to find the node. 
        if node.data > n_val:
            # Look left and while looking assign the value to left node. 
            # This can be confusing but for cases where the a left child's subtree exists, it returns itself to itself.
            # There by not changing anything. 
            node.left = BinaryTree._do_delete(node.left, n_val)
            return node
        
        # Look in the right subtree.
        elif node.data < n_val:
            node.right = BinaryTree._do_delete(node.right, n_val)
            return node
        
        # We found the data to delete.
        elif node.data == n_val:
            # If the left nodes do not exist, we can just return the right child which will go to the delete loop.
            if node.left is None:
                return node.right
            
            elif node.right is None:
                return node.left
            
            # This is where it has 2 children.
            else:
                node.right = BinaryTree.lift(node.right, node)
                return node

    @staticmethod
    def lift(node, node_d):
        if node.left:
            # So, this is the parent of the successor.
            node.left = BinaryTree.lift(node.left, node)
            return node
        else:
            # We found the successor node. No more left children.
            # We replace the node's value with the value 
            node_d.data = node.data
            
            # This will be used at step 114, to be assigned to parents left chid.
            return node.right



    def delete(self, n_val):
        return BinaryTree._do_delete(self.root, n_val)

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
    t.delete(45)
    print("After delete--------------------")
    print(t)
