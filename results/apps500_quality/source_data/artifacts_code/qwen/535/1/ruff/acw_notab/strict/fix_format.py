from fractions import Fraction
from math import gcd

MOD = 7 + 10**9


def expected_value(n, k):
    if k == 0:
        return n

    # Calculate the prime factorization of n
    factors = {}
    temp = n
    for i in range(2, 1 + int(n**0.5)):
        while temp % i == 0:
            if i in factors:
                factors[i] += 1
            else:
                factors[i] = 1
            temp //= i
    if temp > 1:
        factors[temp] = 1

    # Calculate the expected value
    numerator = 1
    denominator = 1
    for prime, exp in factors.items():
        numerator *= sum(Fraction(prime, prime**i) for i in range(exp + 1))
        denominator *= sum(Fraction(1, prime**i) for i in range(exp + 1))

    # Simplify the fraction
    gcd_val = gcd(numerator, denominator)
    numerator //= gcd_val
    denominator //= gcd_val

    # Calculate the modular inverse of the denominator
    inv_denominator = pow(denominator, MOD - 2, MOD)

    # Return the result
    return (inv_denominator * numerator) % MOD


# Read input
n, k = map(int, input().split())

# Print the result
print(expected_value(n, k))
