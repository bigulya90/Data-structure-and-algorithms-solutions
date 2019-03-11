# Given a sorted linked list, delete all duplicates such that each element appear only once.

class NodeList(object):
    def __init__(self, node):
        self.val = node
        self.next = None


class Solution(object):
    def delete_duplicates(self, head):
        if head is None:
            return None

        cur = head

        while cur and cur.next:
            if cur.next.val == cur.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head