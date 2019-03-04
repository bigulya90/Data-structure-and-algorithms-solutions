class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def find_largest_value_in_row(self, root):
        if not root:
            return []

        result = []
        queue = [root]

        while queue:
            max_val = -float("inf")
            level = []

            for node in queue:
                max_val = max(max_val, node.val)
                if node.left:
                    level.append(node.left)

                if node.right:
                    level.append(node.right)

            result.append(max_val)
            queue = level

        return result




