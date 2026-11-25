import math


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def check_sequence(n, m, k, sequence):
    for i in range(1, n + 1):
        row = [gcd(i, j) for j in range(1, m + 1)]
        if row[:k] == sequence:
            return "YES"
    return "NO"


# Read input
n, m, k = map(int, input().split())
sequence = list(map(int, input().split()))

# Output the result
print(check_sequence(n, m, k, sequence))
