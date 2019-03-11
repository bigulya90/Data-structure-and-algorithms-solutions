class LinkedList(object):
    def __init__(self, val):
        self.val = val
        self.next = None


def compare_linked_list(l1, l2):
    while l1 and l2 and l1.val == l2.val:
        l1 = l1.next
        l2 = l2.next

    if l1 and not l2:
        return -1

    if l2 and not l1:
        return -1

    if l1 and l2:
        if l1.val > l2.val:
            return 1
        else:
            return -1

    return 0

