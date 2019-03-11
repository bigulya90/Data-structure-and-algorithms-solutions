class TreeNode(object):
    def __init__(self, value, children):
        self.value = value
        self.children = children


class PostOrder(object):
    def postorder(self, root):

        if not root:
            return []

        output = []
        stack = [root]

        while stack:
            last = stack.pop()
            stack += last.children
            output += [last.value]
        return output[::-1]



