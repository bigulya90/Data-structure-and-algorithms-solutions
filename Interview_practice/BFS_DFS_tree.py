import sys


class Node(object):
    def __init__(self, val):
        self.val = val
        self.children = []

    def get_children(self):
        return self.children

    def add_child(self, node):
        self.children.append(node)

    def get_rev_children(self):
        children = self.children[:]
        children.reverse()
        return children


class Solution(object):
    def bfs_tree(self, root):
        result = []
        stack = [root]  # queque

        while stack:
            cur_node = stack.pop(0)
            result.append(cur_node)

            for i in cur_node.get_children:
                stack.append(i)
        return result

    def dfs_tree(self, root):
        stack = [root]
        result = []

        while stack:
            node = stack.pop(0)
            result.append(node)
            for child in node.get_rev_children():
                stack.insert(0, child)
            return result


def println(text):
    sys.stdout.write(text + "\n")


def make_test_tree():
    a0 = Node("a0")
    b0 = Node("b0")
    b1 = Node("b1")
    b2 = Node("b2")
    c0 = Node("c0")
    c1 = Node("c1")
    d0 = Node("d0")

    a0.add_child(b0)
    a0.add_child(b1)
    a0.add_child(b2)

    b0.add_child(c0)
    b0.add_child(c1)

    c0.add_child(d0)

    return a0


def test_breadth_first_nodes():
    root = make_test_tree()
    node_list = self.bfs_tree(root)
    for node in node_list:
        println(str(node))


if __name__ == "__main__":
    test_breadth_first_nodes()


