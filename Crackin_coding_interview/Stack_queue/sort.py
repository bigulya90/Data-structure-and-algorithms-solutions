"sort stack"

# based on Cracking coding interview soltion: N(n^2)


def sort_stack():
    stack = []
    result = []

    while stack:
        temp = stack.pop()
        while result and result[-1] > temp:
            stack.append(result.pop())

        result.append(temp)

    return result

