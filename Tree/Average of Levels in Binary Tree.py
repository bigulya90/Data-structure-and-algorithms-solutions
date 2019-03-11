class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def find_average(self, root):
        if root is None: return -1

        stack = [root]
        result = []

        while stack:
            count = 0
            n = len(stack)

            for i in range(n):
                node = stack.pop(0)
                count += node.val

                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)

            result.append(count / float(n))
        return result
