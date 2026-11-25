import sys
from collections import defaultdict


def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for num in range(2, 1 + int(limit**0.5)):
        if is_prime[num]:
            for multiple in range(num * num, limit + 1, num):
                is_prime[multiple] = False
    return is_prime


def min_operations_to_flip_all(N, x):
    limit = max(x)
    is_prime, prime_factors = sieve_of_eratosthenes(limit), defaultdict(list)

    for num in x:
        for p in range(3, limit + 1, 2):
            if is_prime[p] and 0 == num % p:
                prime_factors[p].append(num)
                while num % p == 0:
                    num //= p
        if num > 1:
            prime_factors[num].append(num)

    operations = 0
    for p in sorted(prime_factors.keys()):
        operations += len(prime_factors[p])

    return operations


# Read input
N = int(sys.stdin.readline().strip())
x = list(map(int, sys.stdin.readline().strip().split()))

# Output the result
print(min_operations_to_flip_all(N, x))
