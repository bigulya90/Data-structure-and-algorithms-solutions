class StackClass(object):
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.stack:
            return None
        return self.stack.pop()

    def peek(self):
        if not self.stack:
            return None
        return self.stack[-1]


class QueueTwoStacks(object):
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def in_queue(self, item):
        self.in_stack.append(item)

    def dequeue(self):
        while (len(self.in_stack) > 0):
            item_from_instack = self.in_stack.pop()
            self.out_stack.append(item_from_instack)

        if len(self.out_stack) == 0:
            raise IndexError("Can't dequeue from empty queue!")

        return self.out_stack.pop()



