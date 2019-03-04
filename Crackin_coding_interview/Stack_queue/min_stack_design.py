class StackClass(object):
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, item):
        self.stack.append(item)
        if len(self.min_stack) == 0 or self.min_stack[-1] > item:
            self.min_stack.append(item)

    def peek(self):
        item = self.stack[-1]
        return item

    def pop(self):
        item = self.stack.pop()

        if len(self.min_stack) > 0:
            if item == self.min_stack[-1]:
                self.min_stack.pop()

        return item

    def get_min(self):
        if len(self.min_stack) > 0:
            return self.min_stack.pop()

    