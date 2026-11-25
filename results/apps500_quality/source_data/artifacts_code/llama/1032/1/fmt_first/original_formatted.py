import sys


def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return [p for p in range(2, n + 1) if primes[p]]


def get_factors(n):
    factors = set()
    for p in primes:
        if p > n:
            break
        if n % p == 0:
            factors.add(p)
            while n % p == 0:
                n //= p
    if n > 1:
        factors.add(n)
    return factors


def get_prime_factors(n):
    factors = {}
    for p in primes:
        if p > n:
            break
        if n % p == 0:
            factors[p] = factors.get(p, 0) + 1
            while n % p == 0:
                n //= p
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors


n, p = map(int, input().split())
a = list(map(int, input().split()))

max_a = max(a)
min_a = min(a)
total = sum(a)

if min_a > total:
    print(0)
else:
    primes = sieve_of_eratosthenes(max_a)
    factors = get_prime_factors(n)
    result = []
    for x in range(min_a + 1, total + 1):
        prime_factors = get_prime_factors(x)
        if not any(
            p in prime_factors and prime_factors[p] % (factors[p] + 1) == 0
            for p in factors
        ):
            result.append(x)
    print(len(result))
    print(*sorted(result))
