# reverse singly linked list


class NodeClass(object):
    def __init__(self, node):
        self.node = node
        self.next = None

    def reverse(self, node):
        if node is None:
            return None

        cur = node
        prev = None

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        return prev
