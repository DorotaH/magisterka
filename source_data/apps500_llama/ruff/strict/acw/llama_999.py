import math


def count_shichi_go(N):
    def count_divisors(n):
        count = 0
        for i in range(1, int(math.sqrt(n)) + 1):
            if n % i == 0:
                count += 1 if n / i == i else 2
        return count

    def is_perfect_power(k):
        root = int(math.sqrt(k))
        return root**2 == k

    factorial = 1
    for i in range(1, N + 1):
        factorial *= i

    shichi_go_count = 0
    for i in range(1, 1 + factorial):
        if i != 1 and count_divisors(i) == 7 and is_perfect_power(count_divisors(i)):
            shichi_go_count += 1

    return shichi_go_count


N = int(input())
print(count_shichi_go(N))
