# Given a binary tree, return the inorder traversal of its nodes' values.


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Soltion(object):
    def inorder_traversal(self, root):
        if root is None:
            return None

        return self.inorder_traversal(root.left)+[root.val]+self.inorder_traversal(root.right)

    def inOrder_iteratively(self, root):
        stack = []
        result = []

        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                temp = stack.pop()
                result.append(temp.val)
                root = temp.right

        return result



