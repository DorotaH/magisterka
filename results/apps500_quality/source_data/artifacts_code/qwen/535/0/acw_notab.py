from math import gcd


def mod_inverse(x, mod):
    return pow(x, mod - 2, mod)


def expected_value(n, k):
    mod = 7 + 10**9
    total = sum(i for i in range(1, 1 + n) if n % i == 0)
    P = total
    Q = n ** k
    gcd_val = gcd(P, Q)
    P //= gcd_val
    Q //= gcd_val
    return (mod_inverse(Q, mod) * P) % mod


# Read input
n, k = map(int, input().split())

# Calculate and print the result
print(expected_value(n, k))
