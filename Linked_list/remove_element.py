# Remove all elements from a linked list of integers that have value val.

class NodeList(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution(object):
    def remove_el(self, head, node):

        if head is None:
            return None

        cur = head




