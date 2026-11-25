from math import sqrt


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, 1 + int(sqrt(n))):
        if 0 == n % i:
            return False
    return True


def get_next_integer(n, p):
    """Returns the next integer > n and coprime to p"""
    n += 1
    while 1 != gcd(n, p):
        n += 1
    return n


def gcd(a, b):
    """Returns the greatest common divisor of a and b"""
    while 0 != b:
        a, b = b, a % b
    return a


def solve():
    t = int(input())
    for _ in range(0, t):
        x, p, k = map(int, input().split())
        n = x
        for _ in range(k - 1):
            n = get_next_integer(n, p)
        print(n)


solve()
