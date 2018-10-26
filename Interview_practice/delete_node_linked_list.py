# coding=utf-8

"""
Delete a node from a singly-linked list, ↴ given only a variable pointing to that node.
"""


class LinkedList(object):
    def __init__(self, value):
        self.value = value
        self.next = None

    def delete_node(self, node_to_delete):
        next_node = node_to_delete.next
        if next_node:
            node_to_delete.value = next_node.value
            node_to_delete.next = next_node.next

        else:
            raise Exception("Can't delete the last node with this technique!")


a = LinkedList('A')
b = LinkedList('B')
c = LinkedList('C')

a.next = b
b.next = c







