import math


def count_shichi_go(N):
    def count_divisors(n):
        count = 0
        for i in range(1, int(math.sqrt(n)) + 1):
            if 0 == n % i:
                if not n / i == i:
                    count += 2
                else:
                    count += 1
        return count

    def is_perfect_power(k):
        root = int(math.sqrt(k))
        return root * root == k

    factorial = 1
    for i in range(1, N + 1):
        factorial *= i

    shichi_go_count = 0
    for i in range(1, factorial + 1):
        if 1 != i and 7 == count_divisors(i) and is_perfect_power(count_divisors(i)):
            shichi_go_count = shichi_go_count + 1

    return shichi_go_count


N = int(input())
print(count_shichi_go(N))
