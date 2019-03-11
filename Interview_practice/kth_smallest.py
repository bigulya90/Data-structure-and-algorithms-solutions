class BinaryTree(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def helper(self, root, res):
        if not root:
            return None

        if root:
            self.helper(root.left, res)
            res.append(root.val)
            self.helper(root.right, res)

    def smallest(self, root, k):
        if root is None:
            return None

        res = []

        self.helper(root, res)
        return res[k-1]
