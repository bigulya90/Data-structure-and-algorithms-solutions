
def binary(decNumber):
    stack = []

    while decNumber > 0:
        reminder = decNumber % 2
        stack.append(reminder)
        decNumber = decNumber // 2

    binarySt = ''
    while len(stack) != 0:
        binarySt = binarySt + str(stack.pop())
    return binarySt

print (binary(56))
