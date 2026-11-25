import math


def kth_greatest_common_divisor(A, B, K):
    gcd = math.gcd(A, B)
    divisors = [i for i in range(1, gcd + 1) if gcd % i == 0]
    divisors.sort(reverse=True)
    return divisors[K - 1]

# Read input
A, B, K = map(int, input().split())

# Print the result
print(kth_greatest_common_divisor(A, B, K))
