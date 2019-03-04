class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.children = None

    def get_children(self):
        return self.children

    def add_child(self, node):
        self.children.append(node)


# class Solution:
    def level_order_binary_tree(self, root):
        stack = [root]
        result = []

        while stack:
            node = stack.pop(0)
            result.append(node.val)

            if node.left:
                stack.append(node.left)

            if node.right:
                stack.append(node.right)

        return result



    def level_order_n_arry(self, root):
        stack = [root]
        result = []

        while stack:
            node = stack.pop(0)
            result.append(node.val)

            for i in node.children:
                stack.append(i)

        return result








