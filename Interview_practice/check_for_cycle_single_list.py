# coding=utf-8

"""
You have a singly-linked list and want to check if it contains a cycle.
O(n) time and O(1)O(1) space.

"""


def check_for_cycle(first_node):
    slow = first_node
    fast = first_node

    while slow is not None and slow.next is not None:
        slow = slow.next
        fast = fast.next.next

        if fast is slow:
            return True

    return False

