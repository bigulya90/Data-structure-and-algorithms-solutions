# merged two sorted list


class NodeClass(object):
    def __init__(self, node):
        self.node = node
        self.next = None


class Solution(object):
    def merge_list_Recursive(self, l1, l2):
        if l1 is None:
            return l2

        if l2 is None:
            return l1

        if l1.val < l2.val:
            head = l1
            head.next = self.merge_list_Recursive(l1.next, l2)
        else:
            head = l2
            head.next = self.merge_list_Recursive(l1, l2.next)
        return head

    def merge_lest(self, l1, l2):
        if l1 is None:
            return l2

        if l2 is None:
            return l1

        merged = NodeClass(0)
        copy = merged

        while l1 and l2:
            if l1.val < l2.val:
                merged.next = l1
                l1 = l1.next
            else:
                merged.next = l2
                l2 = l2.next
            merged = merged.next

        while l1:
            merged.next = l1
            l1 = l1.next
            merged = merged.next

        while l2:
            merged.next = l2
            l2 = l2.next
            merged = merged.next

        return copy.next

