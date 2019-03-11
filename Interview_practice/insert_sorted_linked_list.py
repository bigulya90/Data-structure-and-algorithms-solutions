class LinkedList(object):
    # Constructor to initialize the node object

    def __init__(self, val):
        self.val = val
        self.next = None

    def insert(self, head, key):
        if head is None:
            head = key
        if head.val > key:
            key.next = head
            head = key

        cur = head

        while cur.next is not None and cur.next.val < key:
            cur = cur.next
        key.next = cur.next
        cur.next = key



