class BinarySearchTree(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def is_balanced(self, root, lower = -float('inf'), upper = ('inf')):
        if root is None:
            return True

        if root.val >= upper or root.val <= lower:
            return False

        return self.is_balanced(root.left, lower, root.val) and self.is_balanced(root.right, root.val, upper)


# O(n) time and O(n)O(n) space.


    def solution2_is_balanced(self, root):
        if root is None:
            return None

        # find height of left and right sub trees
        left_sub = self.get_height(root.left)
        right_sub = self.get_height(root.right)

        if abs(left_sub-right_sub) <= 1 and self.solution2_is_balanced(root.left) is True and self.solution2_is_balanced(root.right) is True:
            return True

        return False

    def get_height(self, root):
        if root is None:
            return None

        return max(self.get_height(root.left), self.get_height(root.right))