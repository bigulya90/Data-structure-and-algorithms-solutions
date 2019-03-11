class NodeClass(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class solution(object):
    def find_middle_poit(self, head):
        slow, fast = head, head

        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def merge(self, head1, head2):
        temp = NodeClass(None)
        node = temp

        while head1 and head2:
            if head1.val < head2.val:
                node.next = head1
                head1 = head1.next
            else:
                node.next = head2
                head2 = head2.next
            node = node.next

        node.next = head1 or head2
        return temp.next

    def sort_list(self, head):
        if head is None or head.next is None:
            return head

        mid_node = self.find_middle_poit(head)
        right_node = mid_node.next
        mid_node.next = None

        return self.merge(self.sort_list(head), self.sort_list(right_node))


