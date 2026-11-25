from math import gcd


def mod_inverse(x, mod):
    return pow(x, mod - 2, mod)


def expected_value(n, k):
    mod = 10**9 + 7
    total = 0
    for i in range(1, n + 1):
        if n % i == 0:
            total = total + i
    P = total
    Q = n**k
    gcd_val = gcd(P, Q)
    P = P // gcd_val
    Q = Q // gcd_val
    return (P * mod_inverse(Q, mod)) % mod


# Read input
n, k = map(int, input().split())

# Calculate and print the result
print(expected_value(n, k))
