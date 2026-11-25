# Importing the required module for large number arithmetic
from functools import reduce


# Function to calculate factorial modulo mod
def factorial(n, mod):
    return reduce(lambda x, y: x * y % mod, range(1, n + 1), 1)

# Function to calculate binomial coefficient modulo mod
def binomial_coefficient(n, k, mod):
    if k > n:
        return 0
    return factorial(n, mod) * pow(factorial(k, mod), mod - 2, mod) * pow(factorial(n - k, mod), mod - 2, mod) % mod

# Reading input
N, K = map(int, input().split())

# Special case when N is 1
if N == 1:
    print(K % (10**9 + 7))
else:
    # For even N, the first and last elements can be any of K values, and the middle N/2 elements can be any of K values
    if N % 2 == 0:
        print((K**2 * binomial_coefficient(N // 2 - 1, N // 4, 10**9 + 7) % (10**9 + 7)) % (10**9 + 7))
    # For odd N, the first and last elements can be any of K values, and the middle (N-1)/2 elements can be any of K values
    else:
        print((K * binomial_coefficient((N - 1) // 2, (N - 3) // 4, 10**9 + 7) % (10**9 + 7)) % (10**9 + 7))
