"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

"""


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def find_max_depth(self, root):
        if root is None:
            return -1

        left_max = self.find_max_depth(root.left)
        right_max = self.find_max_depth(root.right)

        if left_max > right_max:
            return left_max + 1
        else:
            return right_max + 1

