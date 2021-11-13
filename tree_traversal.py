# Traversing the tree.
  def inorderTraversal(self, root):
      """
      Read the left subtree.
      Read the root
      Read the right subtree.
      """
      if not root:
          return
      # Recursively reach the left sub-tree's end.         
      self.inorderTraversal(root.left)
      
      # Print the value of the root.
      self.output.append(root.val)
      
      # Recursively reach the right sub-tree's end.
      self.inorderTraversal(root.right)

      return self.output
