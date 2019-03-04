# Minimum Distance Between BST Nodes


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):

    pre = -float('inf')
    res = float('inf')

    def find_min_diff(self, root):

        if root.left:
            self.find_min_diff(root.left)

        self.res = min(self.res, root.val - self.pre)
        self.pre = root.val

        if root.right:
            self.find_min_diff(root.right)

        return self.res




