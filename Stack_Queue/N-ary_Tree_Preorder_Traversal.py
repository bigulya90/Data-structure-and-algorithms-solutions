class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.children = None

    def preorder_n_ary_tree(self, root):
        if root is None: return []

        stack = [root]
        result = []

        while stack:
            node = stack.pop(0)
            if node:
                result.append(node.val)
                stack += node.children
        return result
