class BinaryTree(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTree(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTree(value)
        return self.right

    def is_balanced(self, root):
        if root is None:
            return True

        stack = []

        stack.append(root)

        #keeping track of the depth as we go.
        depths = []

        while stack:
            curr, depth = stack.pop()

            if (not curr.left and  not curr.right):
                if depth not in depths:
                    depths.append(depth)

                if ((len(depths) > 2) or
                        (len(depths) == 2 and abs(depths[0] - depths[1]) > 1)):
                    return False

            else:
                if curr.left:
                    stack.append((curr.left, depth + 1))
                if curr.right:
                    stack.append((curr.right, depth + 1))

        return True




