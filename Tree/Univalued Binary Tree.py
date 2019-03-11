"""
A binary tree is univalued if every node in the tree has the same value.

Return true if and only if the given tree is univalued.

"""

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def is_tree_univalued(self, root):
        if root is None:
            return []

        stack = [root]
        result = []
        value = root.val

        while stack:
            node = stack.pop()
            if node is not None:
                if value != node.val:
                    return False
                result.append(node.val)
                stack.append(node.left)
                stack.append(node.right)

        return True





