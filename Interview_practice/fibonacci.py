def fib_slow(n):   # 2^n
    if n < 0:
        raise ValueError

    if n in [0, 1]:
        return n
    return fib_slow(n-1) + fib_slow(n-2)

def fib(n):   # O(n) space O(1)
    if n < 0:
        raise ValueError

    if n in [0, 1]:
        return n

    prev_prev = 0
    prev = 1
    cur = 0

    for _ in range(n-1):
        cur = prev + prev_prev
        prev_prev = prev
        prev = cur

    return cur


if __name__ == "__main__":
    print (fib(7))
    print (fib_slow(7))


