import math
import sys


def count_divisors(n):
    count = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if i * i == n:
                count += 1
            else:
                count += 2
    return count


def factorial_divisors(n):
    factors = {}
    for i in range(2, n + 1):
        temp = i
        for j in range(2, int(math.sqrt(temp)) + 1):
            while temp % j == 0:
                if j in factors:
                    factors[j] += 1
                else:
                    factors[j] = 1
                temp //= j
        if temp > 1:
            if temp in factors:
                factors[temp] += 1
            else:
                factors[temp] = 1
    return factors


def shichi_go_numbers(n):
    factors = factorial_divisors(n)
    count = 1
    for key in factors:
        count *= factors[key] + 1
    return count


N = int(sys.stdin.read().strip())
print(shichi_go_numbers(N))
