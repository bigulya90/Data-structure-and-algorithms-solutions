class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def levelOrderTraverse(root):
    if not root:
        return

    queue = []
    queue.append(root)

    while queue:
        print (queue[0].data)
        node = queue.pop(0)

        if node.left is not None:
            queue.append(node.left)

        if node.right is not None:
            queue.append(node.right)



