class NondeClass(object):
    def __init__(self, node):
        self.node = node
        self.next = None

class Solution(object):
    def find_middle(self, node):
        if node is None:
            return None

        slow = node
        fast = node

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

