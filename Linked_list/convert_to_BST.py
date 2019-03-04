# Convert Sorted List to Binary Search Tree

class NodeList(object):
    def __init__(self, val):
        self.node = val
        self.next = None

class Solution(object):
    def sortedListToBST(self, head):
        if head is None:
            return None

        tree = []

        while head:
            tree.append(head.val)
            head = head.next

        root = self.tree_converter(tree)
        return root

    def tree_converter(self, tree):
        if tree is None:
            return None

        mid = len(tree) // 2
        root = NodeList(tree[mid])
        root.left = self.tree_converter(tree[:mid])
        root.right = self.tree_converter(tree[mid+1:])
        return root


