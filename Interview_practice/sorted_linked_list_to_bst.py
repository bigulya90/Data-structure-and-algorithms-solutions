# Convert Sorted List to Binary Search Tree
# Time (nLgn), space O(n)

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class LinkedList(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution(object):
    def build_tree(self, tree):
        if tree is None:
            return

        mid = len(tree) // 2

        root = TreeNode(tree[mid])
        root.left = self.build_tree(tree[:mid])
        root.right = self.build_tree(tree[mid+1 :])
        return root

    def sorted_linked_list(self, head):
        if head is None:
            return None

        tree = []

        while head:
            tree.append(head.val)
            head = head.next

        root = self.build_tree(tree)
        return root


