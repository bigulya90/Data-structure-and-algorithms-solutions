from math import ceil, floor


def karatsuba(x, y):
    # base case
    if x < 10 and y < 10:  # in other words, if x and y are single digits
        return x * y

    n = max(len(str(x)), len(str(y)))
    m = int(ceil(float(n) / 2))  # Cast n into a float because n might lie outside the representable range of integers.

    x_H = int(floor(x / 10 ** m))
    x_L = int(x % (10 ** m))

    y_H = int(floor(y / 10 ** m))
    y_L = int(y % (10 ** m))

    # recursive steps
    a = karatsuba(x_H, y_H)
    d = karatsuba(x_L, y_L)
    e = karatsuba(x_H + x_L, y_H + y_L) - a - d

    return int(a * (10 ** (m * 2)) + e * (10 ** m) + d)

x = 3141592653589793238462643383279502884197169399375105820974944592
y = 2718281828459045235360287471352662497757247093699959574966967627

print(karatsuba(x,y))


def karatsuba2(x, y):
    """Function to multiply 2 numbers in a more efficient manner than the grade school algorithm"""
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x * y
    else:
        n = max(len(str(x)), len(str(y)))
        nby2 = n / 2

        a = x / 10 ** (nby2)
        b = x % 10 ** (nby2)
        c = y / 10 ** (nby2)
        d = y % 10 ** (nby2)

        ac = karatsuba2(a, c)
        bd = karatsuba2(b, d)
        ad_plus_bc = karatsuba2(a + b, c + d) - ac - bd

        # this little trick, writing n as 2*nby2 takes care of both even and odd n
        prod = ac * 10 ** (2 * nby2) + (ad_plus_bc * 10 ** nby2) + bd

        return prod

print karatsuba2(x, y)