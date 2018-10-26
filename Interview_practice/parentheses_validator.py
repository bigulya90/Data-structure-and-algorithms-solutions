"""
"{ [ ] ( ) }" should return True
"{ [ ( ] ) }" should return False
"{ [ }" should return False
"""


def validator(list):
    openers_to_closers = {
        '(': ')',
        '{': '}',
        '[': ']',
    }

    opener = set(openers_to_closers.keys())
    closer = set(openers_to_closers.values())
    stack = []

    for i in list:
        if i in opener:
            stack.append(i)

        elif i in closer:
            if not stack:
                return False
            else:
                last_open = stack.pop()
                if not openers_to_closers[last_open] == i:
                    return False

    return stack == []


list = "{[}()}"
y = validator(list)
print y


def brackets(string_s):

    hash_set = {")": "(",
                "]": "[",
                "}": "{",
                ">": "<"}

    stack = []

    for c in string_s:
        if c in hash_set.values():
            stack.append(c)
        elif not stack:
            return False
        elif stack[-1] == hash_set[c]:
            stack.pop()
    return not stack


print brackets(list)

