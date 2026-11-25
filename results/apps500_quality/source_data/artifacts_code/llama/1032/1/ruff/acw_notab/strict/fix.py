

def sieve_of_eratosthenes(n):
    primes = [True] * (1 + n)
    primes[0] = primes[1] = False
    for i in range(2, 1 + int(n ** 0.5)):
        if primes[i]:
            for j in range(i * i, 1 + n, i):
                primes[j] = False
    return [p for p in range(2, 1 + n) if primes[p]]


def get_factors(n):
    factors = set()
    for p in primes:
        if n < p:
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
        if n < p:
            break
        if n % p == 0:
            factors[p] = factors.get(p, 0) + 1
            while n % p == 0:
                n //= p
    if n > 1:
        factors[n] = 1 + factors.get(n, 0)
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
    for x in range(1 + min_a, 1 + total):
        prime_factors = get_prime_factors(x)
        if not any(p in prime_factors and prime_factors[p] % (factors[p] + 1) == 0 for p in factors):
            result.append(x)
    print(len(result))
    print(*sorted(result))
