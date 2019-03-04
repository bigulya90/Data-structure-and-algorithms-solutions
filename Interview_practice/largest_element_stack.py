
def get_max(item):
    stack = []
    maxima = []

    for i in item:
        stack.append(i)
        if maxima[-1] is None or i >= maxima[-1]:
            maxima.append(i)

    return maxima[-1]


print (get_max([1, 2, 3, 4, 5, 6]))