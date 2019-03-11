class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def isBSTfull(self, root):
        if not root:
            return True

        if not root.left and not root.right:
            return True

        if root.left is not None and root.right is not None:
            return self.isBSTfull(root.left) and self.isBSTfull(root.right)

        return False
