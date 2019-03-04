# find cycle in Linked List

class NodeList(object):
    def __init__(self, node):
        self.val = node
        self.next = None


class Solution(object):
    def find_cycle(self, node):
        if node is None:
            return None

        slow = node
        fast = node.next

        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False