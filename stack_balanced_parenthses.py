"""
Implementing the Simple balanced Parentheses.
Most recent open matches first close.
First open may waint until last close.
"""

def balanced(symbolString):
    stack = []
    open = "("
    close = ")"

    for i in symbolString:
        if i not in open and i not in close:
            print "Invalid symbol"
        elif i in open:
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            stack.pop()
    return len(stack) == 0


print balanced(')(')

def is_matched(expression):
    """
    Finds out how balanced an expression is.
    With a string containing only brackets.

    """
    opening = ('({[')
    closing = (')}]')
    mapping = dict(zip(opening, closing))
    stack = []

    for letter in expression:
        if letter in opening:
            stack.append(mapping[letter])
        elif letter in closing:
            if not stack or letter != stack.pop():
                return False
    return not stack

print is_matched('(){}[]]]]')


def balanced_stack(alist):
    balanced = True
    index = 0

    stack = []

    while index < len(alist) and balanced:
        symbol = alist[index]
        if symbol == "(":
            stack.append(symbol)
        else:
            if len(stack) == 0:
                return False
            else:
                stack.pop()
        index +=1

    if balanced and len(stack) == 0:
        return True
print balanced_stack("()")


def pairCheck(alist):
    stack = []
    balanced = True
    index = 0

    while index < len(alist) and balanced:
        symbol = alist[index]
        if symbol in "([{":
            stack.append(symbol)
        else:
            if len(stack) == 0:
                return False
            else:
                top = stack.pop()
                if not matches(top, symbol):
                    return False
        index += 1

    if balanced and len(stack) == 0:
        return True
    else:
        return False


def matches(open, closing):
    opens = "([{"
    closed = ")]}"

    return opens.index(open) == closed.index(closing)




