import math


def sieve_of_eratosthenes(n):
    """
    Generate a list of primes less than or equal to n
    """
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(math.sqrt(n)) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return [p for p in range(2, n + 1) if primes[p]]


def get_nth_element(x, p, k):
    """
    Get the k-th element of L(x, p)
    """
    primes = sieve_of_eratosthenes(p - 1)
    count = 0
    y = x + 1
    for prime in primes:
        if y > x and math.gcd(y, p) == 1:
            count += 1
            if count == k:
                return y
        y += 1


t = int(input())
for _ in range(t):
    x, p, k = map(int, input().split())
    print(get_nth_element(x, p, k))
