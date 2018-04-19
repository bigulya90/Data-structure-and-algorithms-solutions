'''
Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.
'''


def divide(dividend, divisor):
    """
    :type dividend: int
    :type divisor: int
    :rtype: int
    """
    sign = -1 if ((dividend < 0) ^ (divisor < 0)) else 1

    dividend = abs(dividend)
    divisor = abs(divisor)
    count = 0

    while dividend >= divisor:
        dividend = dividend - divisor
        count += 1
    return count * sign