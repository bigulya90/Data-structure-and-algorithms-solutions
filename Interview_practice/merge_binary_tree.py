"""
Time complexity : O(n)
A total of n nodes need to be traversed. Here, n represents the minimum number of nodes from the two given trees.
Auxiliary Space : O(n)
The depth of the recursion tree can go upto n in case of a skewed tree. In average case, depth will be O(logn).

"""


class NodeTree(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None

    def merge_tree(self, t1, t2):

        if t1 == None:
            return t2

        if t2 == None:
            return t1

        t1.value += t2.value
        t1.left = self.merge_tree(t1.left, t2.left)
        t1.right = self.merge_tree(t1.right, t2.right)
        return t1

    def mergeTrees_iterative(self, t1, t2):

        if t1 is None:
            return t2

        stack = []

        stack.append((t1, t2))

        while stack:
            t = stack.pop()
            if t[1] is None:
                continue
            t[0].val += t[1].val

            if t[0].left is None:
                t[0].left = t[1].left
            else:
                stack.append((t[0].left, t[1].left))

            if t[0].right is None:
                t[0].right = t[1].right
            else:
                stack.append((t[0].right, t[1].right))
        return t1