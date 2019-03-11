# delete given Node, given only access to that node.


class NodeClass(object):
    def __init__(self, node):
        self.node = node
        self.next = None


class Solution:
    
    def delete_node(self, node):
        if node.next:
            node.val = node.val.next
            node.next = node.next.next


