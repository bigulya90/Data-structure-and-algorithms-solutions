# Sort a linked list in O(n log n)


class NodeList(object):
    def __init__(self, val):
        self.node = val
        self.next = None


class Solution(object):
    def sort_linked_list(self, head):
        if head is None:
            return None

        mid = self.find_mid_point(head)
        rigt_node = mid.next
        mid.next = None

        return self.merger_list(self.sort_linked_list(head), self.sort_linked_list(rigt_node))

    def find_mid_point(self, head):
        slow = head
        fast = head

        while fast and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merger_list(self, l1, l2):
        node = NodeList(0)
        temp = node

        while l1 and l2:
            if l1.val < l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next

        node.next = l1 or l2
        return node.next



