class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def merger_two_tree(self, t1, t2):
        if t1 is None:
            return t2

        if t2 is None:
            return t1

        t1.val += t2.val
        t1.left = self.merger_two_tree(t1.left, t2.left)
        t1.left = self.merger_two_tree(t1.right, t2.right)
        return t1


