import math


def sieve_of_eratosthenes(n):
    """
    Generate a list of primes less than or equal to n
    """
    primes = [True] * (1 + n)
    primes[0] = primes[1] = False
    for i in range(2, 1 + int(math.sqrt(n))):
        if primes[i]:
            for j in range(i * i, 1 + n, i):
                primes[j] = False
    return [p for p in range(2, 1 + n) if primes[p]]


def get_nth_element(x, p, k):
    """
    Get the k-th element of L(x, p)
    """
    primes, count = sieve_of_eratosthenes(p - 1), 0
    y = 1 + x
    for prime in primes:
        if x < y and 1 == math.gcd(y, p):
            count += 1
            if k == count:
                return y
        y = y + 1


t = int(input())
for _ in range(0, t):
    x, p, k = map(int, input().split())
    print(get_nth_element(x, p, k))
