# coding=utf-8
# 1. Write a python program to print the square of all numbers from 0 to 10

for i in range(11):
    sqr = i*i
    print sqr

# 2. Write a python program to find the sum of all even numbers from 0 to 10

summ = 0
for n in range(11):
    summ += n
    print "summary ", summ

"""
3. Write a python program to read a number and print the binary of that number (hint: if ‘a’ is a string , a[::-1] will be reverse of that string)

6. Write a python program to read four numbers (representing the four octets of an IP) and print the next five IP address

7. Write a python program to print the factorial of a given number

8. Write a python program to print the first 10 numbers Fibonacci series

9. Write a python program to read a number and print a right triangle using "*"

10. Write a python program to check given number is prime or not

11. Write a python program to print all prime numbers between 0 to 100 , and print how many prime numbers are there.

12. a, b, c = 0, 0, 0 . Write a python program to print all permutations using those three variables
"""

n = 5
for i in range(n):
    for j in range(i):
        print ('* ')
    print

#################

def decimalToBinary(n):
    if (n > 1):
        # divide with integral result
        # (discard remainder)
        decimalToBinary(n // 2)

    print(n % 2)

print decimalToBinary(12)

count = 0
alist = [44]

for i in alist:
    if i % 2 == 0:
        print "not prime"
    print "prime"


def isMonotonic(A):
    """
    :type A: List[int]
    :rtype: bool

    """
    is_monotonic_asc = True
    is_monotonic_desc = True

    for i in range(1, len(A)):
        if A[i] < A[i - 1]:
            is_monotonic_asc = False
        if A[i] > A[i - 1]:
            is_monotonic_desc = False

    return is_monotonic_asc or is_monotonic_desc

print isMonotonic([5,6,7])


print "two sum"
def twoSum(numbers, target):

    for left in numbers:
        for right in range(len(numbers[::-1])):
            if (numbers[left] + numbers[right]) == target:
               return left, right

print twoSum([1, 2, 3, 4, 5], 9)

