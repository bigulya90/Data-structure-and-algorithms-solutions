# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.


class stackClass(object):
    def __init__(self):
        self.stack = []

    def is_valid(self, s):
        stack_dict = {")":"(", "}":"{", "]":"["}
        stack = []

        for i in s:
            if i in stack_dict:
                if not stack:
                    return False
                else:
                    last = stack.pop()
                    if stack_dict[i] != last:
                        return False
            else:
                stack.append(i)

        return not stack

