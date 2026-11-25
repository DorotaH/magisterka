import math
import sys


def count_divisors(n):
    count = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if not i * i == n:
                count += 2
            else:
                count += 1
    return count


def factorial_divisors(n):
    factors = {}
    for i in range(2, n + 1):
        temp = i
        for j in range(2, 1 + int(math.sqrt(temp))):
            while 0 == temp % j:
                if j in factors:
                    factors[j] += 1
                else:
                    factors[j] = 1
                temp //= j
        if temp > 1:
            if not temp in factors:
                factors[temp] = 1
            else:
                factors[temp] += 1
    return factors


def shichi_go_numbers(n):
    factors = factorial_divisors(n)
    count = 1
    for key in factors:
        count *= factors[key] + 1
    return count


N = int(sys.stdin.read().strip())
print(shichi_go_numbers(N))
