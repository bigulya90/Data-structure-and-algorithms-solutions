
"""Time: if balanced tree = O(lgn), otherwise = O(n)
Space : O(1) """


class BinaryTree(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


    def largest_node(self, root):
        if root is None:
            return None

        curr = root

        while curr:
            if not curr.right:
                return curr.val
            curr = curr.right

    def second_largest(self, root):
        if root is None:
            return None

        curr = root

        while curr:
            if curr.left and not curr.right:
                return self.largest_node(curr.left)

            if curr.right and not curr.right.left and not curr.right.right:
                return curr.val

            curr = curr.right
