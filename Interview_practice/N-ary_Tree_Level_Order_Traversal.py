class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.children = None


class Solution(object):

    def level_order(self, root):
        if root is None:
            return []

        result = []
        queue = [root]

        while queue:
            level = []

            for _ in range(len(queue)):
                node = queue.pop(0)
                level.append(node.val)

                queue += node.children
            result.append(level)

        return result


x= Solution()


root = TreeNode(1)
root.children = TreeNode(9)
root.children = TreeNode(20)
root.children = TreeNode(15)
root.children = TreeNode(7)

print (x.level_order(root))


