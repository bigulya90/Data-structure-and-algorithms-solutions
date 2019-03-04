# Given a binary tree, return the postorder traversal of its nodes' values.

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    def post_order(self, root): # since Post Order is reversed version of PreOrder LRH vs HLR, we can implement PreOrder and reversed the solution

        stack = [root]
        result = []

        while stack:
            node = stack.pop()
            if node:
                result.append(node.val)
                stack.append(node.left)
                stack.append(node.right)

        return result[::-1]

    def real_postOrder(self, root):
        if root is None:
            return []

        stack = [root]
        result = []

        while stack:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

            result.insert(0, node.val)

        return result

    def post_order_recursive(self, root):
        if root is None:
            return []

        return (self.post_order_recursive(root.left) + self.post_order_recursive(root.right) + [root.val])

