"""
Given a binary search tree and the lowest and highest boundaries as L and R, trim the tree so that all its elements
lies in [L, R] (R >= L). You might need to change the root of the tree, so the result should return the new root of the
trimmed binary search tree.

Solution:
When node.val > R, we know that the trimmed binary tree must occur to the left of the node.
Similarly, when node.val < L, the trimmed binary tree occurs to the right of the node.
Otherwise, we will trim both sides of the tree.

"""


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def treem_tree(self, root, L, R):
        if root.val > R:
            return self.treem_tree(root.left, L, R)
        elif root.val < L:
            return self.treem_tree(root.right, L, R)
        root.left = self.treem_tree(root.left, L, R)
        root.right = self.treem_tree(root.right, L, R)

        return root


