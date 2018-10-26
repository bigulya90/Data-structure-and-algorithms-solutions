class BinaryTreeNode(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None

    def search_in_bst(self, root, target):
        if not root or root.value == target:
            return root

        if target < root.value:
            return self.search_in_bst(root.left, target)
        else:
            return self.search_in_bst(root.right, target)
