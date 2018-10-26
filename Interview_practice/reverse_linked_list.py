# coding=utf-8

"""
Write a function for reversing a linked list. Do it in place.
input: head of the list
return new head of the list
"""


def reverse(head):
    current = head
    prev = None
    next_node = None

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev