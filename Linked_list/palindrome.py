# Given a singly linked list, determine if it is a palindrome.


class NodeList(object):
    def __init__(self, val):
        self.node = val
        self.next = None


class Solution(object):
    def palindrome_linked_list(self, head):
        if head is None:
            return True

        is_palindrome = False

        stack = []

        while head and head.next:
            stack.append(head.val)
            head = head.next

        if stack == stack[::-1]:
            return True

        return is_palindrome


