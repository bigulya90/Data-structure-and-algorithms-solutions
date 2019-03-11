class LinkedListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def mergeTwoLists(self, l1, l2):
        """
               :type l1: ListNode
               :type l2: ListNode
               :rtype: ListNode
               """
        if not l1 or not l2: return l2 or l1

        while l1 and l2:
            if l1.val < l2.val:
                l1.next = self.mergeTwoLists(l1.next, l2)
                return l1
            else:
                l2.next = self.mergeTwoLists(l2.next, l1)
                return l2

    def merge_in_place(self, l1, l2):
        cur, dummy = LinkedListNode(0)

        dummy.next = l1
        while l1 and l2:
            if l1.val < l2.val:
                l1 = l1.next
            else:
                nxt = cur.next
                cur.next = l2
                tmp = l2.next
                l2.next = nxt
                l2 = tmp

            cur = cur.next
        cur.next = l1 or l2
        return dummy.next
