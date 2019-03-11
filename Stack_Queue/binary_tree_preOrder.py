class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    def preOrder(self, root):

        stack = [root]
        result = []

        while stack:
            node = stack.pop()

            if node:
                result.append(node.val)
                stack.append(node.right)
                stack.append(node.left)

        return result

    def pre_order(self, root):
        return ([root.val] + self.pre_order(root.left) + self.pre_order(root.right))

