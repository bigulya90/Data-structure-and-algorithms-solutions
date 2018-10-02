# def fact(n):
#     if n <= 0:
#         return 1
#     else:
#         # n*(n-1)
#         return n * fact(n-1)
#
# print (fact(4))

def fib(n):
    if n >=3:
        return fib(n-1) + fib(n-2)
    else:
        return 1

print fib(5)