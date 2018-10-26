st1 = "abc"
st2 = "cf"


def string_in_stack(st1, st2):
    # create empty stack
    stack1 = []
    stack2 = []

    # insert all char from string to stack one by one
    for ch in st1:
        stack1.append(ch)
    print "Printing first stack ", stack1

    for ch in st2:
        stack2.append(ch)
    print "Printing second stack ", stack2

    # concatenate two stacks
    stack3 = stack1 + stack2
    print "Main stack ", stack3

    # pop char from stack
    stack3.pop()
    print "stack after singl pop ", stack3

    # pop all char from stack
    while stack3:
        stack3.pop()
    print "stack after all pop ", stack3


string_in_stack(st1, st2)


def string_in_dict(st1, st2):
    alphabetDict = dict()

    for char in st1:
        char = alphabetDict.keys()

    print alphabetDict



string_in_dict(st1, st2)





def find_shortest_path(st1, st2):
    if len(st1) >= len(st2):
        short = st2
        long = st1
    else:
        short = st1
        long = st2

    stack = []




