class StackClass(object):
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, item):
        self.in_stack.append(item)

    def dequeue(self):
        if len(self.out_stack) == 0 :
            while len(self.in_stack) > 0:
                latest_node = self.in_stack.pop()
                self.out_stack.append(latest_node)

        return self.out_stack.pop()
    
