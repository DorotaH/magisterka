from math import sqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def get_next_integer(n, p):
    """Returns the next integer > n and coprime to p"""
    n += 1
    while gcd(n, p) != 1:
        n += 1
    return n

def gcd(a, b):
    """Returns the greatest common divisor of a and b"""
    while b != 0:
        a, b = b, a % b
    return a

def solve():
    t = int(input())
    for _ in range(t):
        x, p, k = map(int, input().split())
        n = x
        for _ in range(k - 1):
            n = get_next_integer(n, p)
        print(n)

solve()
