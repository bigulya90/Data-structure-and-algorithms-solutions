class Stack(object):
    # Initialize the empty stack
    def __init__(self):
        self.stack = []

    def push(self, item):
        # Add new item
        self.stack.append(item)

    def pop(self):
        # Remove item
        if not self.stack:
            return None
        return self.stack.pop()

    def peek(self):
        # Get the last value in the stack
        if not self.stack:
            return None
        return self.stack[-1]


class MaxStack(object):
    def __init__(self):
        self.stack = Stack()
        self.max_stack = Stack()

    def push(self, item):
        self.stack.push(item)
        if self.max_stack.peek() is None or item >= self.max_stack.peek():
            self.max_stack.push(item)

    def pop(self):
        item = self.stack.pop()
        if item == self.max_stack.peek():
            self.max_stack.peek()

        return item

    # return the lagest elelment in the stack
    def get_max(self):
        return self.max_stack.peek()



