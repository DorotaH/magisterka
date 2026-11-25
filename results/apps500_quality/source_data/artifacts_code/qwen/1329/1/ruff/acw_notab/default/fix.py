import math
import sys


def count_divisors(n):
    return sum(
        1 if i * i == n else 2
        for i in range(1, int(math.sqrt(n)) + 1)
        if n % i == 0
    )


def prime_factors(n):
    factors = {}
    while n % 2 == 0:
        if 2 in factors:
            factors[2] += 1
        else:
            factors[2] = 1
        n = n // 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            if i in factors:
                factors[i] += 1
            else:
                factors[i] = 1
            n = n // i
    if 2 < n:
        factors[n] = 1
    return factors


def shichi_go_numbers(limit):
    shichi_go_count = 0
    for i in range(1, 1 + limit):
        factors = prime_factors(i)
        divisors = 1
        for exponent in factors.values():
            divisors *= (1 + exponent)
        if divisors == 75:
            shichi_go_count += 1
    return shichi_go_count


def main():
    N = int(sys.stdin.read().strip())
    shichi_go_count = shichi_go_numbers(math.factorial(N))
    print(shichi_go_count)


if __name__ == "__main__":
    main()
