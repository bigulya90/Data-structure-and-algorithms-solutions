# Both approaches use O(n)O(n) time and O(1)O(1) space.

class LinkedListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def kth_to_last_node(self, head, k):
        if head is None:
            return None

        if k < 1:
            raise ValueError("")

        left_node = head
        right_node = head

        for i in range(k-1):
            if not right_node.next:
                raise ValueError("")
            right_node = right_node.next

        while right_node.next:
            left_node = left_node.next
            right_node = right_node.next

        return left_node

    def second_solution(self, k, head):
        length = 1
        curr = head

        while curr:
            curr = curr.next
            length += 1

        if k > length:
            raise ValueError("")

        second_walk = length - 1

        current = head
        for i in range(second_walk):
            current = current.next
        return current.next


