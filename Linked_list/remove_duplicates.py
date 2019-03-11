# Remove Duplicates from Sorted List II

class NodeList(object):
    def __init__(self, val):
        self.node = val
        self.next = None

class Solution(object):
    def remove_duplicates(self, head):
        