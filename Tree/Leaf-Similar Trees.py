class TreeNode():
    def __init__(self, node):
        self.node = node
        self.left = None
        self.right = None

    def find_leaf(self, root):
        if not root: return None
        if not root.left and not root.right:
            return root.val
        return self.find_leaf(root.left) + self.find_leaf(root.right)

    def leafSimilar(self, root1, root2):
        return self.find_leaf(root1) == self.find_leaf(root2)