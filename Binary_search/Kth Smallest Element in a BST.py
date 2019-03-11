# Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def smallest(self, root):

       cur = root

       while cur:
           if not cur.left:
               return cur.val
           cur = cur.left


    def find_kth_smallest(self, root, k):
        if root is None:
            return None
        stack = []

        while True:
            while root:
                stack.append(root)
                root = root.left

            if not stack:
                return

            node = stack.pop()
            k -= 1
            if k == 0:
                return node.val
            root = node.right

